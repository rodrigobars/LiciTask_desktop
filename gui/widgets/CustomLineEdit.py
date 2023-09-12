# IMPORT QT CORE
from qt_core import *

class CustomLineEdit(QLineEdit):
    def __init__(self, MinimumWidth=110, MaximumWidth=110, isFilePath=False):
        super().__init__()

        # Set default parametros
        self.setMinimumWidth(MinimumWidth)
        self.setMaximumWidth(MaximumWidth)
        
        self.setMinimumHeight(30)
        self.setMaximumHeight(30)

        if isFilePath:
            font_size = '9pt'
        else:
            font_size = '12pt'
        
        style = f"""
        QLineEdit {{
            color: black;
            font: 600 {font_size} 'Segoe UI';
            padding-left: 10px;
            background-color: transparent;
            border-style: none none solid none;
            border-width: 0 0 2px 0;
            border-color: black;
        }}
        QLineEdit:hover {{
            border-color: blue;
        }}
        """

        self.setAlignment(Qt.AlignLeft)

        self.setStyleSheet(style)