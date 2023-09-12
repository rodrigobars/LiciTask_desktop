from qt_core import *

from src.modules.scrap_to_excel import scrap_to_excel

# IMPORT CUSTOM WIDGETS
from gui.widgets.CustomLineEdit import CustomLineEdit
from gui.widgets.CustomLabel import CustomLabel
from gui.widgets.CustomButtonFind import CustomButtonFind
from gui.widgets.CustomButtonStart import CustomButtonStart

def Page_3(obj, root, application_pages):
    def open_file_dialog_excel():
        file_path, _ = QFileDialog.getOpenFileName(application_pages, "Selecionar Arquivo")
        if file_path:
            obj.save_path_page3_input.setText(file_path.replace('/', '\\'))

    def start():
        obj.botao_iniciar_page3.setEnabled(False)
        scrap_to_excel(       
            pregao = obj.num_pregao_page3_input.text(),
            excel_path = obj.save_path_page3_input.text()
        )
        obj.botao_iniciar_page3.setEnabled(True)

    obj.page_3 = QFrame()
    obj.page_3.setObjectName(u"Scan de pregão em andamento")
    obj.verticalLayout_3 = QGridLayout(obj.page_3)
    obj.verticalLayout_3.setObjectName(u"verticalLayout_3")

    obj.num_pregao_page3_label = CustomLabel(text="Número do pregão:")
    obj.num_pregao_page3_input = CustomLineEdit()
    obj.num_pregao_page3_input.setPlaceholderText("Ex: 12023")
    obj.verticalLayout_3.addWidget(obj.num_pregao_page3_label, 0, 0)
    obj.verticalLayout_3.addWidget(obj.num_pregao_page3_input, 0, 1)

    obj.save_path_page3_label = CustomLabel(text="Caminho da planilha:")
    obj.save_path_page3_input = CustomLineEdit(MinimumWidth=120, MaximumWidth=1200, isFilePath=True)
    obj.save_path_page3_input.setReadOnly(True)
    obj.botao_save_page3_path = CustomButtonFind()
    obj.botao_save_page3_path.clicked.connect(open_file_dialog_excel)
    obj.verticalLayout_3.addWidget(obj.save_path_page3_label, 1, 0)
    obj.verticalLayout_3.addWidget(obj.save_path_page3_input, 1, 1)
    obj.verticalLayout_3.addWidget(obj.botao_save_page3_path, 1, 2)

    # Iniciar
    obj.botao_iniciar_page3 = CustomButtonStart()
    obj.botao_iniciar_page3.clicked.connect(start)
    obj.verticalLayout_3.addWidget(obj.botao_iniciar_page3, 2, 0)

    application_pages.addWidget(obj.page_3)