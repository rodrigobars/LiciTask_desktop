import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QToolButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurações da janela principal
        self.setWindowTitle("Janela Principal")
        self.setGeometry(0, 0, 300, 200)
        self.center_window()

        # Cria um widget central para armazenar o layout
        widget = QWidget(self)
        self.setCentralWidget(widget)

        # Layout vertical para a janela principal
        layout = QVBoxLayout(widget)
        layout.setAlignment(Qt.AlignCenter)

        # Cria o botão
        self.button = QToolButton()
        self.button.setIcon(QIcon("arrow_icon.png"))  # Substitua "arrow_icon.png" pelo caminho do seu ícone
        self.button.clicked.connect(self.open_new_window)
        layout.addWidget(self.button)

    def center_window(self):
        # Obtém o objeto QScreen para a tela primária
        primary_screen = QApplication.primaryScreen()
        screen_geometry = primary_screen.availableGeometry()

        # Calcula as coordenadas para centralizar a janela
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2

        # Define as coordenadas para centralizar a janela
        self.move(x, y)

    def open_new_window(self):
        new_window = NewWindow(self)
        self.hide()
        new_window.show()

    def closeEvent(self, event):
        # Certifica-se de que a aplicação é encerrada quando a janela principal é fechada
        QApplication.quit()


class NewWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Configurações da nova janela
        self.setWindowTitle("Nova Janela")
        self.setGeometry(0, 0, 300, 200)
        self.center_window()

        # Cria um widget central para armazenar o layout
        widget = QWidget(self)
        self.setCentralWidget(widget)

        # Layout vertical para a nova janela
        layout = QVBoxLayout(widget)
        layout.setAlignment(Qt.AlignCenter)

        # Cria o botão de retorno
        return_button = QToolButton()
        return_button.setIcon(QIcon(r"C:\Users\Rodrigo.DESKTOP-ST2DND8\Downloads\arrow.png"))  # Substitua "arrow_icon.png" pelo caminho do seu ícone
        return_button.clicked.connect(self.return_to_main_window)
        layout.addWidget(return_button)

    def center_window(self):
        # Obtém o objeto QScreen para a tela primária
        primary_screen = QApplication.primaryScreen()
        screen_geometry = primary_screen.availableGeometry()

        # Calcula as coordenadas para centralizar a janela
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2

        # Define as coordenadas para centralizar a janela
        self.move(x, y)

    def return_to_main_window(self):
        self.parent().show()
        self.close()

    def closeEvent(self, event):
        # Certifica-se de que a aplicação é encerrada quando a nova janela é fechada
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
