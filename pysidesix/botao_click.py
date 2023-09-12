import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class RoundButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(100, 100)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Desenha o círculo preenchido
        painter.setBrush(QColor(255, 0, 0))
        painter.drawEllipse(0, 0, self.width(), self.height())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurações da janela principal
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:transparent;")

        # Cria o botão redondo
        button = RoundButton(self)
        button.clicked.connect(self.on_button_clicked)

        # Define o botão como widget central
        self.setCentralWidget(button)

    def on_button_clicked(self):
        print("Botão redondo clicado!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
