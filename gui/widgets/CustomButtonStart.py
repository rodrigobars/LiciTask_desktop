# IMPORT QT CORE
from qt_core import *

class CustomButtonStart(QPushButton):
    def __init__(self):
        super().__init__()

        # Set default parametros
        self.setMinimumWidth(100)
        self.setMaximumWidth(100)
        
        self.setMinimumHeight(30)
        self.setMaximumHeight(30)

        self.setText("Iniciar")

        self.setCursor(Qt.PointingHandCursor)

        style = f"""
        QPushButton {{
            background-color: rgba(63, 94, 251, 0.7);
            color: black;
            font: 600 9pt 'Segoe UI';
            border-radius: 10px;
            padding: 0px 12px;
        }}
        QPushButton:hover {{
            background-color: rgba(63, 94, 251, 1);
        }}
        QPushButton:pressed {{
            background-color: rgba(63, 94, 251, 0.85);
        }}
        """

        self.setStyleSheet(style)