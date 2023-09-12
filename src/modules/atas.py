def atas(pregao, data_elaboracao, dou, ata_path, term_path):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    from time import sleep
    import pyautogui as gui
    import win32com.client as win32
    import os

    # Limpando o gen.py antes de ocorrer erro
    #os.system("powershell Remove-Item -path $env:LOCALAPPDATA\Temp\gen_py -recurse")
    #os.system("cls")

    def get_month(data):
        month = {
            1: "Janeiro",
            2: "Fevereiro",
            3: "Março",
            4: "Abril",
            5: "Maio",
            6: "Junho",
            7: "Julho",
            8: "Agosto",
            9: "Setembro",
            10: "Outubro",
            11: "Novembro",
            12: "Dezembro"
        }
        return month.get(int(data[3:5]))


    def startWord():
        try:
            #os.system("cls")
            # Abrindo o programa Word e setando a visibilidade como verdadeira
            global word
            word = win32.gencache.EnsureDispatch('Word.Application')
            word.Visible = True

            # Abrindo o caminho do documento Word
            wordDoc = word.Documents.Open(rf'{ata_path}')
            #gui.getWindowsWithTitle('Word')[0].minimize()

            # Consertando os títulos
            wordDoc.Content.GoTo(3, 1, 1).Select()
            find = word.Selection.Find
            find.Text = "ANEXO III DO EDITAL DO "
            find.Replacement.Text = ""
            find.Execute(Replace=1, Forward=True)
            find.Text = "MINUTA "
            find.Execute(Replace=1, Forward=True)

            # Inserindo a data de publicação
            # Lembrando que é necessário remover o highlight
            wordDoc.Content.GoTo(3, 1, 1).Select()
            find = word.Selection.Find

            find.Text = "xx/xx/20xx"

            find.Replacement.Text = f"{dou}"
            find.Replacement.Highlight = False
            find.Execute(Replace=1, Forward=True)

            wordDoc.Content.GoTo(3, 1, 1).Select()

            # Apaga todas as tabelas do documento
            n_tables = len(word.ActiveDocument.Tables)

            for i in range(1, n_tables+1):
                word.ActiveDocument.Tables(i).Delete()

            # Preenchendo com dia de hoje
            wordDoc.Content.GoTo(3, 1, 1).Select()

            find.Text = "Niterói, RJ, ____ de ___________"
            find.Replacement.Text = f"Niterói, RJ, {data_elaboracao[0:2]} de {get_month(data_elaboracao)}"
            find.Execute(Replace=1, Forward=True)
        except Exception as e:
            print(e)

        return wordDoc, term_path

    #####################################
    # Abrindo o navegador para o início #
    #####################################

    # Implementar o Type Annotation


    def runStartWork(wordDoc):
        print("Iniciando a estruturação da ata de registro de preços...")
        content = wordDoc.Content
        content.Find.Text = "proposta(s) são as que seguem:"
        content.Find.Execute(Forward=True)

        # Colocando o cursor no final do documento
        CurPos = content.Words(1).End
        # Pegando o número de parágrafos até a ocorrência da palavra do content que é um "Find"
        NumParagraphs = wordDoc.Range(0, CurPos).Paragraphs.Count

        # Iniciando o carregamento da página
        url = "http://comprasnet.gov.br/livre/pregao/ata0.asp"

        # Informando o Path para o arquivo "chromedriver.exe" e armazenando em "driver"

        op = webdriver.ChromeOptions()
        #op.add_argument("--headless")
        op.add_experimental_option("excludeSwitches", ["enable-logging"])

        # Format Path
        app_path = os.path.abspath(os.getcwd())
        
        # Chromebrowser path
        chrome_folder = "chrome-driver/chrome-win64/chrome.exe"
        chrome_path = os.path.join(app_path, chrome_folder)

        # Chromedriver path
        driver_folder = "chrome-driver/chromedriver-win64/chromedriver.exe"
        driver_path = os.path.join(app_path, driver_folder)

        # Informando o navegador que será utilizado
        op.binary_location = chrome_path

        # Informando o caminho do chromedriver
        driver = webdriver.Chrome(service=ChromeService(driver_path), options=op)
            
        # Abrindo o google chrome no site informado
        driver.get(url)

        # Navegador em tela cheia
        driver.maximize_window()

        # Configurando o tempo de espera em segundos até que o elemento html seja encontrado
        wdw = WebDriverWait(driver, 2000)

        CodUasg = wdw.until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='co_uasg']"))
        )
        CodUasg.send_keys("150182")

        NumPreg = wdw.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@id='numprp']")))
        NumPreg.send_keys(pregao)

        driver.execute_script("ValidaForm();")

        PrClick = wdw.until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[contains(text(), '{}')]".format(pregao))
            )
        )
        PrClick.click()

        Owners = wdw.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='btnResultadoFornecr']")
            )
        )
        Owners.click()

        # Armazena a quantidade total de empresas vencedoras
        num_companys = driver.find_elements(By.XPATH, "//td[contains(text(), 'Item')]").__len__()
        
        print(f"Empresas: {num_companys}")

        indexStartEnd = [1]
        companyInfo = {}
        start = 0
        end = 2
        startRealIndex = 1
        for company in range(1, num_companys+1):
            driver.execute_script(
                '''window.getElementByXpath = function (path){
                    return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}
                '''
            )

            sleep(1)

            # Preciso checar quantos itens a empresa tem...
            indexStartEnd = driver.execute_script(f"""
                // Selecionando a empresa na tabela
                range = document.createRange();
                sel = window.getSelection();
                sel.removeAllRanges();
                var root_node = document.getElementsByClassName("td")[0];
                range.setStart(root_node.getElementsByClassName('tex3')[{start}], 1);
                range.setEnd(root_node.getElementsByClassName('tex3b')[{end}], 1);
                sel.addRange(range);

                // Retornando o índice do 'start'
                var childStart = root_node.getElementsByClassName('tex3')[{start}]
                var parent = childStart.parentNode
                var indexStart = Array.prototype.indexOf.call(parent.children, childStart)

                // Retornando o índice do 'end'
                var childEnd = root_node.getElementsByClassName('tex3b')[{end}]
                var parent = childEnd.parentNode
                var indexEnd = Array.prototype.indexOf.call(parent.children, childEnd)

                // Retornando o CNPJ
                var cnpj = window.getElementByXpath('/html/body/table[2]/tbody/tr[{startRealIndex}]/td/b').textContent

                // Retornando o NOME
                var name = window.getElementByXpath('/html/body/table[2]/tbody/tr[{startRealIndex}]/td/text()').textContent

                //removi do array cnpj, name
                return Array(indexStart, indexEnd, cnpj, name) 
            """)
            cnpj = indexStartEnd[2].rstrip()
            name = indexStartEnd[3][3:].rstrip()
            companyInfo.update({cnpj: name})
            ###########################################################################################
            # Preciso usar essa informação pra formatar a primeira linha do word e elaborar os termos #
            ###########################################################################################

            gui.hotkey('ctrl', 'c')

            wordDoc.Paragraphs.Add(wordDoc.Paragraphs(NumParagraphs+1).Range)
            wordDoc.Paragraphs.Add(wordDoc.Paragraphs(NumParagraphs+1).Range)
            wordDoc.Paragraphs.Add(wordDoc.Paragraphs(NumParagraphs+1).Range)
            wordDoc.Paragraphs.Add(wordDoc.Paragraphs(NumParagraphs+1).Range)
            wordDoc.Content.Paragraphs(NumParagraphs+2).Range.Paste()
            wordDoc.Paragraphs.Add(wordDoc.Paragraphs(NumParagraphs+1).Range)
            wordDoc.Paragraphs.Add(wordDoc.Paragraphs(NumParagraphs+1).Range)
            wordDoc.Paragraphs.Add(wordDoc.Paragraphs(NumParagraphs+1).Range)
            wordDoc.Paragraphs.Add(wordDoc.Paragraphs(NumParagraphs+1).Range)


            companyItens = int(((indexStartEnd[1]-indexStartEnd[0])-3)/2)
            start += int((companyItens*2)+1)
            end += 3
            startRealIndex += int((companyItens*2)+4)

        # Fechando o navegador
        driver.quit()

        # Varredura de colunas
        for i in range(1, num_companys+1):
            actual_table = wordDoc.Tables(i)
            endOfTable = False
            line = 3

            # Removendo e Mesclando o cabeçalho
            actual_table.Cell(2, 5).Range.Delete()
            actual_table.Cell(2, 4).Merge(wordDoc.Tables(i).Cell(2, 5))

            # Varredura de linhas da tabela atual
            while endOfTable == False:
                try:
                    actual_table.Cell(line, 5).Range.Delete()
                    actual_table.Cell(line, 4).Merge(
                        wordDoc.Tables(i).Cell(line, 5))
                    actual_table.Cell(line+1, 0).Range.Select()
                    word.Selection.Paragraphs.Alignment = 0
                    line += 2
                except:
                    endOfTable = True

            # Colocando borda na tabela atual
            for j in range(1, 5):
                border = wordDoc.Tables(i).Borders.Item(-j)
                border.LineStyle = 21

            # Formatando as informações de cada empresa
            companyInfoDisplay = f"RAZÃO SOCIAL: {list(companyInfo.values())[abs(num_companys-i)]} \nCNPJ: {list(companyInfo.keys())[abs(num_companys-i)]}"

            actual_table = wordDoc.Tables(i)
            actual_table.Cell(1, 1).Range.Delete()
            actual_table.Cell(1, 1).Range.InsertAfter(companyInfoDisplay)

            # textSelected = actual_table.Cell(1, 1).Range.Font
            # textSelected.Name = "Calibri"
            # textSelected.Size = "10,5"
            # textSelected.Bold = True

        # Salva as alterações pendentes no mesmo arquivo automaticamente, sem solicitar ao usuário se -1
        wordDoc.Close(-1, 0)

        return companyInfo


    def startTerms(companyInfo, term_path):
        word = win32.gencache.EnsureDispatch('Word.Application')
        word.Visible = False

        print("Iniciando a elaboração dos termos de responsabilidade...")

        for idx, (cnpj, empresa) in enumerate(companyInfo.items()):
            sleep(1)
            print(f"({cnpj}) - {empresa}")
            # Lembrando que a procura parte de onde o cursos está para frente, por isso é necessário colocá-lo no início
            # Removendo parte do título
            if cnpj == list(companyInfo.keys())[0]:
                wordDoc = word.Documents.Open(rf'{term_path}')  
                sleep(1)
                wordDoc.Content.GoTo(3, 1, 1).Select()
                find = word.Selection.Find
                find.Text = "ANEXO IV DO EDITAL DO "
                find.Replacement.Text = " "
                find.Execute(Replace=1, Forward=True)
                sleep(1)
                # Preenchendo com o nome da empresa
                wordDoc.Content.GoTo(3, 1, 1).Select()
                find.Text = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
                find.Replacement.Text = f"{empresa}"
                find.Replacement.Highlight = False
                find.Execute(Replace=1, Forward=True)
                sleep(1)
                # Preenchendo com o cnpj da empresa
                wordDoc.Content.GoTo(3, 1, 1).Select()
                find.Text = "XXXXXXXXXXXXXXXXXXXXXXX"
                find.Replacement.Text = f"{cnpj}"
                find.Replacement.Highlight = False
                find.Execute(Replace=1, Forward=True)

                # Preenchendo com dia de hoje
                wordDoc.Content.GoTo(3, 1, 1).Select()
                find.Text = "____"
                find.Replacement.Text = f"{data_elaboracao[0:2]}"
                find.Execute(Replace=1, Forward=True)

                # Preenchendo com o mês de hoje
                wordDoc.Content.GoTo(3, 1, 1).Select()
                find.Text = "___________"
                find.Replacement.Text = f"{get_month(data_elaboracao)}"
                find.Execute(Replace=1, Forward=True)
                sleep(1)
                wordDoc.SaveAs2(
                    rf"{os.path.dirname(term_path)}\{(' '.join(empresa.split()[0:2]).replace('/', '.')).upper()}.docx", 16)
            else:
                # Preenchendo com o nome da empresa
                wordDoc.Content.GoTo(3, 1, 1).Select()
                find.Text = valueAux
                find.Replacement.Text = f"{empresa}"
                find.Replacement.Highlight = False
                find.Execute(Replace=1, Forward=True)
                sleep(1)
                # Preenchendo com o cnpj da empresa
                wordDoc.Content.GoTo(3, 1, 1).Select()
                find.Text = keyAux
                find.Replacement.Text = f"{cnpj}"
                find.Replacement.Highlight = False
                find.Execute(Replace=1, Forward=True)
                sleep(1)
                wordDoc.SaveAs2(
                    rf"{os.path.dirname(term_path)}\{(' '.join(empresa.split()[0:2]).replace('/', '.')).upper()}.docx", 16)
                sleep(1)
            keyAux = cnpj
            valueAux = empresa

        with open(rf"{os.path.dirname(term_path)}\\mails.txt", 'w') as mails:
            for companyName in companyInfo.values():
                mails.write(f"{' '.join(companyName.split()[0:2]).upper()};\n")

        word.Quit()

    try:
        wordDocTerm = startWord()
        companyInfo = runStartWork(
            wordDoc=wordDocTerm[0])
        startTerms(companyInfo=companyInfo, term_path=wordDocTerm[1])
        print("Finalizado \U0001F7E2")
    except:
        word.Quit()