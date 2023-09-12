def irp(Login, Senha, NúmeroIRP, Path, inicio, insert_obs, teste):
    import pandas as pd
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.select import Select
    from selenium.webdriver.chrome.service import Service as ChromeService
    from math import ceil
    from time import sleep
    import os

    ############################################################################

    def ProceedSecurity(driver):
        buttonDetails = driver.find_element(By.ID, "details-button")
        if buttonDetails:
            buttonDetails.click()
            driver.find_element(By.ID, "proceed-link").click()


    def CritérioDeValor(driver):
        wdw = WebDriverWait(driver, 20)
        CritériodeValor = wdw.until(
            EC.presence_of_element_located((By.ID, "idCriterioValorCombo"))
        )
        Selected = Select(CritériodeValor)
        Selected.select_by_index(2)

    def PreçoUni(x, driver):
        wdw = WebDriverWait(driver, 20)
        ValorUnitário = wdw.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="div_Item"]/table[2]/tbody/tr[2]/td[5]/input')
            )
        )
        ValorUnitário.clear()
        ValorUnitário.send_keys(str(round(x * 1000, 2)))

    def ValorSigiloso(driver):
        wdw = WebDriverWait(driver, 20)
        ValorSigiloso = wdw.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//input[@type='radio' and @name='item.valorCaraterSigiloso' and @value='2']",
                )
            )
        )
        ValorSigiloso.click()

    def Descrição(x, driver):
        # Verificando se o primeiro campo de descrição está usado...
        try:
            driver.find_element(By.XPATH, 
                "//textarea[contains(@class, 'fieldReadOnly')]")
            Segundo = driver.find_element(By.XPATH, 
                "//textarea[contains(@name, 'item.descricaoComplementar')]"
            )
            Segundo.clear()
            Segundo.send_keys(x)

        except:
            Primeiro = driver.find_element(By.XPATH, 
                "//textarea[contains(@name, 'item.descricaoDetalhada')]"
            )
            Primeiro.clear()
            Primeiro.send_keys(x)

    def localEquantidade(x, driver):
        sleep(0.5)
        try:
            driver.execute_script("javascript:excluirLocalidade(0);")
        except:
            pass
        driver.find_element(By.NAME, 'itemIRPMunicipioEntrega.municipio.nome').send_keys('Niterói/RJ')
        sleep(0.5)
        driver.execute_script('consultarMunicipio(this);')
        sleep(0.5)
        Janelas = driver.window_handles
        driver.switch_to.window(Janelas[1])
        sleep(0.5)
        driver.execute_script("window.opener.retornarConsultaMunicipio('58653;Niterói/RJ');window.close();")
        sleep(1)
        driver.switch_to.window(Janelas[0])
        qtd = driver.find_element(By.XPATH, 
            '//*[@id="div_Item"]/fieldset/table/tbody/tr[2]/td[3]/input'
        )
        qtd.send_keys(str(x))
        sleep(0.5)
        driver.execute_script("incluiMunicipio('divLocaisEntregaItemIRP');")
        sleep(1)

    def WindowManager(driver):
        sleep(1)
        Janelas = driver.window_handles
        try:
            driver.switch_to.window(Janelas[1])
            driver.find_element(By.XPATH, 
                "//title[contains(text(), 'Catálogo de materiais/serviços')]"
            )
            # Segunda janela é de CatMat (Correto)
        except:
            try:
                secundário = Janelas[2]
                driver.close()
                driver.switch_to.window(secundário)
                # Aqui 3 janelas foram abertas, como a segunda janela não é a de CatMat, fechamos ela e damos foco a segunda.
            except:
                if len(Janelas) == 2:
                    # Na arquitetura do código, quando chega aqui o atual handle é [0]
                    driver.switch_to.window(Janelas[1])
                    driver.close()
                    driver.switch_to.window(Janelas[0])
                    # Aqui na hora de salvar abriu um pop-up, portanto, devemos fecha-lo

    def CloseNotification(driver):
        Janelas = driver.window_handles
        if len(Janelas)==2:
            atual = Janelas[0]
            driver.switch_to.window(Janelas[1])
            driver.close()
            driver.switch_to.window(atual)


    def Inclusão_Item(x, driver, inicio, insert_obs, teste):

        if teste == True:
            fim = inicio+1
        else:
            fim = x.shape[0]

        for item in range(inicio, fim):
            while True:
                # Ele precisa ir para a página de onde pertence o item
                if (item+1)>20:
                    aux = (item+1)/20
                    if type(aux) == int:
                        driver.find_element(By.XPATH, f"//a[@title='Ir para página {aux}']").click()
                    else:
                        aux = ceil(aux)
                        driver.find_element(By.XPATH, f"//a[@title='Ir para página {aux}']").click()
                sleep(2)

                # Auxílio no index, pois todas as páginas vão de 1 à 20, sem importar 
                aux2 = (item+1)%20 if item+1>20 else item+1
                if aux2 == 0:
                    aux2 = 20
                sleep(1)

                driver.find_element(By.XPATH, f"//*[@id='itensIRP']/tbody/tr[{aux2}]/td[9]/a").click()

                sleep(1)
                CloseNotification(driver)

                # Seleciona o critério de valor
                CritérioDeValor(driver)

                # Seleciona o preço unitário
                PreçoUni(x.iloc[item, 4], driver)

                # Seleciona o valor sigiloso
                ValorSigiloso(driver)

                # Preenche a descrição
                if insert_obs == True:
                    Descrição(f"Fornecimento de acordo com a especificação contida no Termo de Referência. {x.iloc[item, 0]}", driver)
                else:
                    Descrição(x.iloc[item, 0], driver)

                # Preenche a quantidade
                localEquantidade(x.iloc[item, 3], driver)

                # Por fim, é necessário salvar
                ####Elemento final da programação####
                sleep(0.5)
                driver.execute_script("alterarItemIRP();")

                sleep(1)
                WindowManager(driver)
                driver.execute_script('cancelarAlteracaoInclusaoItemIRP()')
                sleep(2)
                WindowManager(driver)
                sleep(1)

                campo_verificacao = driver.find_element(By.XPATH, f"//*[@id='itensIRP']/tbody/tr[{aux2}]/td[6]")
                if campo_verificacao.text:
                    break

    def extract_excel(path):
        def localizador_indice(df, target_text):
            for index, row in df.iterrows():
                for column in df.columns:
                    cell_value = str(row[column])
                    if target_text.lower() in cell_value.lower():
                        return index, column
                    
        # Leitura da base de dados
        dados = pd.read_excel(path, header=None)
        
        index_item = localizador_indice(dados, 'ITEM')
        index_total = localizador_indice(dados, 'VALOR TOTAL')
        
        drop_list = list(range(index_item[0]))+[index_total[0]]
        dados.drop(drop_list, inplace=True)
        header = dados.iloc[0].values
        dados = dados.iloc[1:,:]
        dados.columns = header
        dados.set_index(header[0], inplace=True)
        
        dados[header[2]] = dados[header[2]].astype(int)
        dados[header[3]] = dados[header[3]].astype(str)
        dados[header[4]] = dados[header[4]].astype(int)
        dados[header[5]] = dados[header[5]].astype(float).round(2)
        
        return dados

    BaseDado = extract_excel(Path)

    inicio = int(inicio) - 1

    # Chamada de tela
    url = "https://www.comprasnet.gov.br/seguro/loginPortal.asp"

    # Informando o Path para o arquivo "chromedriver.exe" e armazenando em "driver"
    op = webdriver.ChromeOptions()
    op.add_argument("--start-maximized")
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
    driver = webdriver.Chrome(service=ChromeService(driver_path), options=op)

    driver.get(url)

    wdw = WebDriverWait(driver, 20)

    # necessário verificar confirmação de segurança
    # id="details-button"
    # id="proceed-link"
    
    ProceedSecurity(driver)

    # Selecionando perfil "Governo"
    wdw.until(
        EC.element_to_be_clickable((By.ID, "card2"))
    )

    driver.execute_script("mudaPerfilBotao(2)")

    # Digitando o CPF
    cpf = driver.find_element(By.ID, "txtLogin")
    cpf.send_keys(Login)
    sleep(0.1)

    # Digitando a SENHA
    senha = driver.find_element(By.ID, "txtSenha")
    senha.send_keys(Senha)
    sleep(0.1)

    # Pressionando o botão "ACESSAR"
    
    driver.execute_script("frmLoginGoverno_submit(); return false;")
    
    sleep(5)

    # Entrando na IRP
    dropdownMenuUser = wdw.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='dropdownMenuUser']"))
    )
    dropdownMenuUser.click()


    IrpModule = wdw.until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'IRP')]"))
    )
    IrpModule.click()

    # ---  Nível de acesso = https://www.comprasnet.gov.br/seguro/indexgov.asp ---
    # Alterando entre Frames do site
    sleep(4)
    atual = driver.window_handles[1]
    driver.close()
    driver.switch_to.window(atual)

    ProceedSecurity(driver)
    irpmodule2 = wdw.until(EC.element_to_be_clickable(((By.ID, "mi_0_5"))))
    irpmodule2.click()

    IrpModule3 = wdw.until(EC.element_to_be_clickable((By.ID, "mi_0_7")))
    IrpModule3.click()

    NumIrp = driver.find_element(By.XPATH, 
        '//*[@id="corpo"]/form/table/tbody/tr[1]/td/table/tbody/tr[3]/td/input'
    )
    NumIrp.click()

    Parâmetro = driver.find_element(By.XPATH, 
        '//*[@id="numeroIrp"]/table/tbody/tr/td/input'
    )
    Parâmetro.send_keys(NúmeroIRP)

    driver.find_element(By.XPATH, '//*[@id="btnConsultar"]').click()

    driver.find_element(By.XPATH, 
        '//*[@id="listaIrps"]/tbody/tr/td[7]/a').click()

    driver.execute_script(
        "try{closeCalendar();}catch(e){};if(document.forms['manterIRPForm'].elements['irp.codigoIrp'].value != ''){ manterIRPForm.abaVisivelAtual.value=2;AlternarAbas('td_Item','div_Item');showHideBotaoDivulgar();showHideBarraBotaoIRP();}"
    )

    # Chamando a função de inclusão de itens:
    Inclusão_Item(BaseDado, driver, inicio, insert_obs, teste)
    print("\n\n\nSUCESSO!\n\n\n")