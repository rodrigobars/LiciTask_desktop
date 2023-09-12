from qt_core import *

from src.modules.atas import atas

# IMPORT CUSTOM WIDGETS
from gui.widgets.CustomLineEdit import CustomLineEdit
from gui.widgets.CustomQDateEdit import CustomQDateEdit
from gui.widgets.CustomLabel import CustomLabel
from gui.widgets.CustomButtonFind import CustomButtonFind
from gui.widgets.CustomButtonStart import CustomButtonStart

def Page_1(obj, root, application_pages):

    def open_file_dialog_ata():
        file_path, _ = QFileDialog.getOpenFileName(application_pages, "Selecionar Arquivo")
        if file_path:
            obj.page_1.file_path_input_ata.setText(file_path.replace('/', '\\'))

    def open_file_dialog_termo():
        file_path, _ = QFileDialog.getOpenFileName(application_pages, "Selecionar Arquivo")
        if file_path:
            obj.page_1.file_path_input_termo.setText(file_path.replace('/', '\\'))

    def start():
        obj.botao_iniciar.setEnabled(False)
        root.hide()

        atas(
            pregao = obj.page_1.num_pregao_input.text(), 
            data_elaboracao = obj.page_1.DataElaboracao.text(), 
            dou = obj.page_1.Dou.text(),
            ata_path = obj.page_1.file_path_input_ata.text(),
            term_path = obj.page_1.file_path_input_termo.text()
        )

        root.show()
        obj.botao_iniciar.setEnabled(True)

    obj.page_1 = QFrame()
    obj.page_1.setObjectName(u"Ata e Termos de Responsabilidade")
    obj.verticalLayout_1 = QGridLayout(obj.page_1)
    obj.verticalLayout_1.setObjectName(u"verticalLayout_1")

    # Número de pregão
    obj.page_1.num_pregao_label = CustomLabel(text="Número do pregão:")
    obj.page_1.num_pregao_input = CustomLineEdit()
    obj.page_1.num_pregao_input.setPlaceholderText("Ex: 12023")

    obj.verticalLayout_1.addWidget(obj.page_1.num_pregao_label, 0, 0)
    obj.verticalLayout_1.addWidget(obj.page_1.num_pregao_input, 0, 1)

    # Data de elaboração
    obj.page_1.DataElaboracao_label = CustomLabel(text="Data de elaboração:")
    obj.page_1.DataElaboracao = CustomQDateEdit()
    obj.page_1.DataElaboracao.setDate(QDate.currentDate())
    obj.page_1.DataElaboracao.setCalendarPopup(True)
    obj.verticalLayout_1.addWidget(obj.page_1.DataElaboracao_label, 1, 0)
    obj.verticalLayout_1.addWidget(obj.page_1.DataElaboracao, 1, 1)

    # Data do DOU
    obj.page_1.Dou_label = CustomLabel(text="Data de publicação:")
    obj.page_1.Dou = CustomQDateEdit()
    obj.page_1.Dou.setDate(QDate.currentDate())
    obj.page_1.Dou.setCalendarPopup(True)
    obj.verticalLayout_1.addWidget(obj.page_1.Dou_label, 2, 0)
    obj.verticalLayout_1.addWidget(obj.page_1.Dou, 2, 1)

    # Ata
    obj.page_1.file_path_label_ata = CustomLabel("Caminho da ata:")
    obj.page_1.file_path_input_ata = CustomLineEdit(MinimumWidth=120, MaximumWidth=1200, isFilePath=True)
    obj.page_1.file_path_input_ata.setReadOnly(True)
    obj.page_1.botao_arquivo_ata = CustomButtonFind()
    obj.page_1.botao_arquivo_ata.clicked.connect(open_file_dialog_ata)

    obj.verticalLayout_1.addWidget(obj.page_1.file_path_label_ata, 3, 0)
    obj.verticalLayout_1.addWidget(obj.page_1.file_path_input_ata, 3, 1)
    obj.verticalLayout_1.addWidget(obj.page_1.botao_arquivo_ata, 3, 2)

    #obj.verticalLayout_1.setColumnStretch(3, 2)

    # Termo
    obj.page_1.file_path_label_termo = CustomLabel("Caminho do termo:")
    obj.page_1.file_path_input_termo = CustomLineEdit(MinimumWidth=120, MaximumWidth=1200, isFilePath=True)
    obj.page_1.file_path_input_termo.setReadOnly(True)
    obj.page_1.botao_arquivo_termo = CustomButtonFind()
    obj.page_1.botao_arquivo_termo.clicked.connect(open_file_dialog_termo)

    obj.verticalLayout_1.addWidget(obj.page_1.file_path_label_termo, 4, 0)
    obj.verticalLayout_1.addWidget(obj.page_1.file_path_input_termo, 4, 1)
    obj.verticalLayout_1.addWidget(obj.page_1.botao_arquivo_termo, 4, 2)

    # Iniciar
    obj.page_1.botao_iniciar = CustomButtonStart()
    obj.page_1.botao_iniciar.setEnabled(True)
    obj.page_1.botao_iniciar.clicked.connect(start)
    obj.verticalLayout_1.addWidget(obj.page_1.botao_iniciar, 5, 0)

    #obj.verticalLayout_1.setColumnStretch(1, 3)
    application_pages.addWidget(obj.page_1)

    return obj