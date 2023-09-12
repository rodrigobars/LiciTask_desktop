import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QToolButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface Principal")

        # Layout principal
        self.layout = QVBoxLayout()

        # Campo de entrada
        self.input_field = QLineEdit()
        self.layout.addWidget(self.input_field)

        # Botão para abrir a primeira "interface"
        button1 = QPushButton("Abrir Interface 1")
        button1.clicked.connect(self.open_interface1)
        self.layout.addWidget(button1)

        # Botão para abrir a segunda "interface"
        button2 = QPushButton("Abrir Interface 2")
        button2.clicked.connect(self.open_interface2)
        self.layout.addWidget(button2)

        # Widget central
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def return_button(self):
        # Cria o botão de retorno
        return_button = QToolButton()
        return_button.setIcon(QIcon(r"C:\Users\Rodrigo.DESKTOP-ST2DND8\Documents\GitHub\App\src\testes\arrow.png"))
        return_button.clicked.connect(self.restore_widgets)
        return_button.setProperty("class", "back-button")
        self.layout.addWidget(return_button)

    def clean_interface(self):
        # Remove todos os widgets do layout principal
        while self.layout.count():
            item = self.layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def open_interface1(self):
        # Remove todos os widgets do layout principal
        while self.layout.count():
            item = self.layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        self.return_button()

        # Novos widgets da primeira "interface"
        label = QLabel("Esta é a Interface 1")
        self.layout.addWidget(label)

        

    def open_interface2(self):
        self.clean_interface()
        self.return_button()

        # Novos widgets da segunda "interface"
        label = QLabel("Esta é a Interface 2")
        self.layout.addWidget(label)

    def restore_widgets(self):
        self.clean_interface()

        # Restaura os widgets originais da interface principal
        self.input_field = QLineEdit()
        self.layout.addWidget(self.input_field)

        button1 = QPushButton("Abrir Interface 1")
        button1.clicked.connect(self.open_interface1)
        self.layout.addWidget(button1)

        button2 = QPushButton("Abrir Interface 2")
        button2.clicked.connect(self.open_interface2)
        self.layout.addWidget(button2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Estilizando o botão de voltar
    app.setStyleSheet("""
    .back-button {
        background-color: transparent;
        color: white;
        border: 1px solid transparent;
        border-radius: 12px;
        padding: 2px;
        font-weight: bold;
    }

    .back-button:hover{
        background-color: #FFF111;
    }
    """)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
