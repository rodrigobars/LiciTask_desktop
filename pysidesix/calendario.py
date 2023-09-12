import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QCalendarWidget, QLabel, QVBoxLayout, QDialog, QWidget
from PySide6.QtCore import Qt

class CalendarDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.WindowFlags(Qt.FramelessWindowHint))
        self.setWindowTitle("Selecione uma data")
        self.calendar = QCalendarWidget(self)
        self.calendar.clicked.connect(self.date_selected)

        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        self.setLayout(layout)

    def date_selected(self):
        date = self.calendar.selectedDate()
        self.selected_date = date.toString("dd/MM/yyyy")
        self.accept()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo de Interface")
        self.button = QPushButton("Selecionar Data", self)
        self.button.clicked.connect(self.open_calendar)
        self.label = QLabel(self)
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def open_calendar(self):
        dialog = CalendarDialog(self)
        if dialog.exec() == QDialog.Accepted:
            selected_date = dialog.selected_date
            self.label.setText(f"Data selecionada: {selected_date}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
