# IMPORT QT CORE
from qt_core import *


class CustomButtonFind(QPushButton):
    def __init__(self):
        super().__init__()

        # Set default parametros
        self.setMinimumWidth(40)
        self.setMaximumWidth(40)
        
        self.setMinimumHeight(40)
        self.setMaximumHeight(40)

        self.setCursor(Qt.PointingHandCursor)

        # Defina o ícone no botão
        self.setIcon(QIcon("gui/images/icons/procurar.png"))

        style = f"""
        QPushButton {{
            background-color: transparent;
            color: white;
            font-size: 16px;
            border-radius: 20px;
            icon-size: 30px;
        }}
        QPushButton:hover {{
            background-color: #AAACCC;
        }}
        QPushButton:pressed {{
            background-color: qlineargradient(x1:0.7, y1:0.6, x2:0.45, y2:0.2, stop:0 rgb(238, 9, 121), stop:1 rgb(255, 106, 0));;
        }}
        """

        self.setStyleSheet(style)