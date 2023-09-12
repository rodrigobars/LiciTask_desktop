from qt_core import *

from src.modules.irp import irp

# IMPORT CUSTOM WIDGETS
from gui.widgets.CustomLineEdit import CustomLineEdit
from gui.widgets.CustomLabel import CustomLabel
from gui.widgets.CustomButtonFind import CustomButtonFind
from gui.widgets.CustomButtonStart import CustomButtonStart
from gui.widgets.CustomQCheckBox import CustomQCheckBox

def Page_4(obj, root, application_pages):
    def open_file_dialog_excel():
        file_path, _ = QFileDialog.getOpenFileName(application_pages, "Selecionar Arquivo")
        if file_path:
            obj.page_4.path_input.setText(file_path.replace('/', '\\'))

    def start():
        obj.botao_iniciar.setEnabled(False)
        root.hide()
        irp(       
            Login = obj.page_4.login_input.text(),
            Senha = obj.page_4.senha_input.text(),
            NúmeroIRP = obj.page_4.irp_input.text(),
            Path = obj.page_4.path_input.text(),
            inicio = obj.page_4.item_inicial_input.text(),
            insert_obs = obj.page_4.observacao.isChecked(),
            teste = obj.page_4.teste.isChecked()
        )
        obj.botao_iniciar.setEnabled(True)
        root.show()

    obj.page_4 = QFrame()
    obj.page_4.setObjectName(u"Scan de pregão em andamento")
    obj.page_4.verticalLayout = QGridLayout(obj.page_4)
    obj.page_4.verticalLayout.setObjectName(u"verticalLayout_4")
    #obj.page_4.verticalLayout.setSpacing(15)

    obj.page_4.login_label = CustomLabel(text="Login:")
    obj.page_4.login_input = CustomLineEdit()
    obj.page_4.login_input.setPlaceholderText("Insira seu login...")
    obj.page_4.verticalLayout.addWidget(obj.page_4.login_label, 0, 0)
    obj.page_4.verticalLayout.addWidget(obj.page_4.login_input, 0, 1)

    obj.page_4.senha_label = CustomLabel(text="Senha:")
    obj.page_4.senha_input = CustomLineEdit()
    obj.page_4.senha_input.setPlaceholderText("Insira sua senha...")
    obj.page_4.verticalLayout.addWidget(obj.page_4.senha_label, 1, 0)
    obj.page_4.verticalLayout.addWidget(obj.page_4.senha_input, 1, 1)

    obj.page_4.irp_label = CustomLabel(text="Insira a IRP:")
    obj.page_4.irp_input = CustomLineEdit()
    obj.page_4.irp_input.setPlaceholderText("Ex: 52023")
    obj.page_4.verticalLayout.addWidget(obj.page_4.irp_label, 2, 0)
    obj.page_4.verticalLayout.addWidget(obj.page_4.irp_input, 2, 1)

    obj.page_4.path_label = CustomLabel(text="Caminho da planilha:")
    obj.page_4.path_input = CustomLineEdit(MinimumWidth=120, MaximumWidth=1600, isFilePath=True)
    obj.page_4.path_input.setPlaceholderText("Insira a planilha...")
    obj.page_4.path_input.setReadOnly(True)
    obj.page_4.botao_path = CustomButtonFind()
    obj.page_4.botao_path.clicked.connect(open_file_dialog_excel)
    obj.page_4.verticalLayout.addWidget(obj.page_4.path_label, 3, 0)
    obj.page_4.verticalLayout.addWidget(obj.page_4.path_input, 3, 1)
    obj.page_4.verticalLayout.addWidget(obj.page_4.botao_path, 3, 2)

    obj.page_4.item_inicial_label = CustomLabel(text="Inserir a partir do item:")
    obj.page_4.item_inicial_input = CustomLineEdit()
    spacer = QSpacerItem(2, 50, QSizePolicy.Minimum)
    obj.page_4.verticalLayout.addWidget(obj.page_4.item_inicial_label, 4, 0)
    obj.page_4.verticalLayout.addWidget(obj.page_4.item_inicial_input, 4, 1)
    obj.page_4.verticalLayout.addItem(spacer, 5, 0)
    

    obj.page_4.observacao_label = CustomLabel(text='Inserir observação:')
    obj.page_4.observacao = CustomQCheckBox()
    obj.page_4.verticalLayout.addWidget(obj.page_4.observacao_label, 6, 0)
    obj.page_4.verticalLayout.addWidget(obj.page_4.observacao, 6, 1)

    obj.page_4.teste_label = CustomLabel(text='Teste:')
    obj.page_4.teste = CustomQCheckBox()
    obj.page_4.verticalLayout.addWidget(obj.page_4.teste_label, 7, 0)
    obj.page_4.verticalLayout.addWidget(obj.page_4.teste, 7, 1)

    # Iniciar
    spacer = QSpacerItem(2, 50, QSizePolicy.Minimum)
    obj.page_4.botao_iniciar = CustomButtonStart()
    obj.page_4.verticalLayout.addItem(spacer, 8, 0)
    obj.page_4.botao_iniciar.clicked.connect(start)
    obj.page_4.verticalLayout.addWidget(obj.page_4.botao_iniciar, 9, 0)
    

    application_pages.addWidget(obj.page_4)