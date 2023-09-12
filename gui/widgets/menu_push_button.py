# IMPORTS
import os

# IMPORT QT CORE
from qt_core import *

class MenuPushButton(QPushButton):
    def __init__(
        self,
        text = "",
        height = 50,
        minimum_width = 50,
        text_padding = 55,
        text_color = "#c3ccdf",
        icon_path = "",
        btn_color = "#44475a",
        btn_hover = "#4f5368",
        btn_pressed = "#282a36",
        is_active = False,
    ):
        super().__init__()

        self.set_icon(icon_path)

        # Set default parametros
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # Custom parameters
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active

        # Set style
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = self.is_active
        )
    
    def set_active(self, is_active_menu):
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = is_active_menu
        )

    def set_style(
        self,
        text_padding = 55,
        text_color = "#c3ccdf",
        btn_color = "#44475a",
        btn_hover = "#4f5368",
        btn_pressed = "#282a36",
        is_active = False
    ):
        style = f"""
        QPushButton {{
            color: {text_color};
            background-color: {btn_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
        }}
        QPushButton:hover {{
            background-color: {btn_hover};
        }}
        QPushButton:pressed {{
            background-color: {btn_pressed};
        }}
        """

        active_style = f"""
        QPushButton {{
            background-color: {btn_hover};
            border-right: 5px solid qlineargradient(x1:0.7, y1:0.6, x2:0.45, y2:0.2, stop:0 rgb(238, 9, 121), stop:1 rgb(255, 106, 0));
        }}
        """
        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)

    def set_icon(self, icon_path):
        # Ícone
        self.icon_layout = QHBoxLayout(self)
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/icons"
        path = os.path.join(app_path, folder)
        icon_path_img = os.path.normpath(os.path.join(path, icon_path))

        # Carrega o ícone
        icon = QIcon(icon_path_img)

        # Criação do QLabel para exibir o ícone
        icon_label = QLabel()
        icon_label.setPixmap(icon.pixmap(23, 23))  # Ajuste o tamanho do ícone conforme necessário

        # Definindo o estilo CSS com background-color transparente
        icon_label.setStyleSheet("background-color: transparent;")

        # Adiciona o QLabel e o texto ao layout do botão
        self.icon_layout.addWidget(icon_label)

        # Define o alinhamento do layout
        self.icon_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.icon_layout.setContentsMargins(13,0,0,0)
        

        # Salvando a cor de estilo dos ícones:
        # primeiro ponto = rgba(238, 9, 121, 1)
        # segundo ponto = rgba(255, 106, 0, 1)

        # Icone #FBE1E1