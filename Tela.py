from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from ModuloInserir import inserir
from ModuloConverterData import converterData

class TelaPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        carregador = QUiLoader()
        self.tela = carregador.load("Tela4.ui")
        self.componentes()
    
    def componentes(self):
        self.caixaData = self.tela.findChild(QtWidgets.QDateTimeEdit, "caixaDatadaViagem")
        self.caixaNome = self.tela.findChild(QtWidgets.QLineEdit, "caixaNomedoCliente")
        self.caixaOrigem = self.tela.findChild(QtWidgets.QLineEdit, "caixaLocaldeOrigem")
        self.caixaDestino = self.tela.findChild(QtWidgets.QLineEdit, "caixaLocaldeDestino")
        self.caixaForma = self.tela.findChild(QtWidgets.QLineEdit, "caixaFormasdePagamento")
        self.btnCadastrar = self.tela.findChild(QtWidgets.QPushButton, "btnCadastrar")
        self.btnCadastrar.clicked.connect(self.cadastrarProducao)

    def cadastrarProducao(self):
        data = self.caixaData.text()
        nome = self.caixaNome.text()
        origem = self.caixaOrigem.text()
        destino = self.caixaDestino.text()
        forma = self.caixaForma.text
        inserir(converterData(data),nome, origem, destino, forma)

    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    interface = TelaPrincipal()
    interface.tela.showMaximized()
    app.exec()