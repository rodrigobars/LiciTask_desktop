from qt_core import *

from src.modules.text_result import text_result

# IMPORT CUSTOM WIDGETS
from gui.widgets.CustomLineEdit import CustomLineEdit
from gui.widgets.CustomLabel import CustomLabel
from gui.widgets.CustomButtonFind import CustomButtonFind
from gui.widgets.CustomButtonStart import CustomButtonStart

def Page_2(obj, root, application_pages):

    def open_file_dialog_dou():
        folder_path = QFileDialog.getExistingDirectory(application_pages, "Selecionar pasta")
        if folder_path:
            obj.save_path_input_page2.setText(folder_path.replace('/', '\\'))

    def start():
        obj.botao_iniciar.setEnabled(False)
        text_result(
            pregao = obj.num_pregao_input_page2.text(),
            path = obj.save_path_input_page2.text()
        )
        obj.botao_iniciar.setEnabled(True)

    obj.page_2 = QFrame()
    obj.page_2.setObjectName(u"Texto de publicação")
    obj.verticalLayout_2 = QGridLayout(obj.page_2)
    obj.verticalLayout_2.setObjectName(u"verticalLayout_2")

    obj.num_pregao_label_page2 = CustomLabel(text="Número do pregão:")
    obj.num_pregao_input_page2 = CustomLineEdit()
    obj.num_pregao_input_page2.setPlaceholderText("Ex: 12023")
    obj.verticalLayout_2.addWidget(obj.num_pregao_label_page2, 0, 0)
    obj.verticalLayout_2.addWidget(obj.num_pregao_input_page2, 0, 1)

    obj.save_path_label = CustomLabel(text="Salvar em:")
    obj.save_path_input_page2 = CustomLineEdit(MinimumWidth=120, MaximumWidth=1200, isFilePath=True)
    obj.save_path_input_page2.setReadOnly(True)
    obj.botao_save_path = CustomButtonFind()
    obj.botao_save_path.clicked.connect(open_file_dialog_dou)
    obj.verticalLayout_2.addWidget(obj.save_path_label, 1, 0)
    obj.verticalLayout_2.addWidget(obj.save_path_input_page2, 1, 1)
    obj.verticalLayout_2.addWidget(obj.botao_save_path, 1, 2)

    # Iniciar
    obj.botao_iniciar = CustomButtonStart()
    obj.botao_iniciar.clicked.connect(start)
    obj.verticalLayout_2.addWidget(obj.botao_iniciar, 2, 0)

    application_pages.addWidget(obj.page_2)