# IMPORT QT CORE
from qt_core import *

class CustomLabel(QLabel):
    def __init__(self, text):
        super().__init__()

        # Set default parametros
        self.setMinimumWidth(120)
        self.setMaximumWidth(180)
        
        self.setMinimumHeight(10)
        self.setMaximumHeight(30)
        
        self.setText(text)

        style = f"""
        QLabel {{
            color: black;
            font: 600 9pt 'Segoe UI';
            padding-right: 10px;
        }}
        """

        self.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.setStyleSheet(style)