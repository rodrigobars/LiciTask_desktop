from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout, QWidget, QFileDialog, QTextEdit
from PySide6.QtCore import QThread, Signal

class WorkerThread(QThread):
    output = Signal(str)  # Sinal para enviar a saída do código

    def __init__(self, num_pregao, senha):
        super().__init__()
        self.num_pregao = num_pregao
        self.senha = senha

    def run(self):
        # Execute o código na thread separada
        # Simule o processamento
        for i in range(200):
            output_text = f"Processando {i+1}..."
            self.output.emit(output_text)
            self.msleep(1)  # Aguarde 1 segundo

def main():
    num_pregao = num_pregao_input.text()
    senha = senha_input.text()

    if not worker.isRunning():  # Verifique se a thread já está em execução
        worker.output.connect(output_text.append)  # Conecte o sinal de saída ao campo de saída
        botao_entrar.setEnabled(False)  # Desativar o botão enquanto o código é executado
        worker.num_pregao = num_pregao  # Atualize os valores de num_pregao e senha
        worker.senha = senha
        worker.start()  # Inicie a thread para executar a função main() em segundo plano

        # Aumentar a largura da janela para 900px
        window.setFixedWidth(800)

        # Exibir o campo de saída
        output_text.setVisible(True)

def open_file_dialog():
    file_path, _ = QFileDialog.getOpenFileName(window, "Selecionar Arquivo")
    if file_path:
        file_path_input.setText(file_path)

app = QApplication([])
window = QMainWindow()
window.setWindowTitle("Interface de ata")
window.setFixedWidth(500)

# Crie uma instância única do WorkerThread
worker = WorkerThread("", "")

# Restante do código permanece o mesmo...

# Criar widgets
num_pregao_label = QLabel("num_pregao:")
num_pregao_input = QLineEdit()
num_pregao_input.setPlaceholderText("Digite seu num_pregao...")
senha_label = QLabel("Senha:")
senha_input = QLineEdit()
senha_input.setPlaceholderText("Digite sua senha...")
senha_input.setEchoMode(QLineEdit.Password)
file_path_label = QLabel("Caminho do Arquivo:")
file_path_input = QLineEdit()
file_path_input.setReadOnly(True)
botao_arquivo = QPushButton("Abrir Arquivo")
botao_arquivo.clicked.connect(open_file_dialog)
botao_entrar = QPushButton("Entrar")
botao_entrar.clicked.connect(main)
output_text = QTextEdit()  # Campo de saída
output_text.setReadOnly(True)  # Torna o campo de saída somente leitura
output_text.setVisible(False)  # Oculta o campo de saída inicialmente

# Estilizar widgets usando QSS
window.setStyleSheet("""
    QWidget {
        background-color: #f0f0f0;
    }
    QLabel {
        font-size: 16px;
        color: #333333;
    }
    QLineEdit {
        font-size: 16px;
        padding: 8px;
        border: 1px solid #cccccc;
        border-radius: 5px;
    }
    QPushButton {
        font-size: 16px;
        padding: 8px;
        background-color: #337ab7;
        color: #ffffff;
        border-radius: 5px;
    }
    QTextEdit {
        font-size: 16px;
        padding: 8px;
        border: 1px solid #cccccc;
        border-radius: 5px;
    }
""")

# Layout
layout = QGridLayout()
layout.addWidget(num_pregao_label, 0, 0)
layout.addWidget(num_pregao_input, 0, 1)
layout.addWidget(senha_label, 1, 0)
layout.addWidget(senha_input, 1, 1)
layout.addWidget(file_path_label, 2, 0)
layout.addWidget(file_path_input, 2, 1)
layout.addWidget(botao_arquivo, 3, 0)
layout.addWidget(botao_entrar, 3, 1)
layout.addWidget(output_text, 0, 2, 4, 1)  # Campo de saída ocupa duas colunas na posição (0, 2) e tem rowspan de 4

layout.setColumnStretch(1, 2)
#layout.setColumnStretch(2, 2)  # Esticar a coluna 2 para ocupar o espaço disponível

# Widget principal
widget = QWidget()
widget.setLayout(layout)
window.setCentralWidget(widget)

window.show()
app.exec()
