# IMPORT QT CORE
from qt_core import *

class CustomQDateEdit(QDateEdit):
    def __init__(self):
        super().__init__()

        # Set default parameters
        self.setMinimumWidth(110)
        self.setMaximumWidth(110)

        self.setMinimumHeight(30)
        self.setMaximumHeight(30)

        style = """
        QDateEdit {
            color: black;
            font: 600 12pt 'Segoe UI';
            padding-left: 3px;
            background-color: transparent;
            border-style: none none solid none;
            border-width: 0 0 2px 0;
            border-color: black;
        }
        QDateEdit:hover {
            border-color: #555555;
        }
        QCalendarWidget QTableView {
            background-color: #333333;
            color: white;
        }
        QCalendarWidget QTableView::item {
            padding: 5px;
            background-color: #555555;
        }
        QCalendarWidget QTableView::item:selected {
            background-color: magenta;
        }
        QCalendarWidget QTableView::item:hover {
            background-color: black;
        }
        QCalendarWidget QToolButton {
            background-color: black;
            color: white;
        }
        QCalendarWidget QToolButton:hover {
            background-color: #555555;
        }
        QCalendarWidget QWidget#qt_calendar_navigationbar {
            background-color: black;
            color: white;
        }
        """

        self.setAlignment(Qt.AlignLeft)
        self.setStyleSheet(style)
