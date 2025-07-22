import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import QSize,QTimer
from teste import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.icone_plutao = QIcon("img/plutao.png")
        self.icone_mercurio = QIcon("img/mercurio.png")
        self.icone_marte = QIcon("img/marte.png")
        self.icone_venus = QIcon("img/venus.png")
        self.icone_terra = QIcon("img/terra.png")
        self.icone_netuno = QIcon("img/netuno.png")
        self.icone_urano = QIcon("img/uranus.png")
        self.icone_saturno = QIcon("img/saturno.png")
        self.icone_jupiter = QIcon("img/jupiter.png")
 
 
        self.ui.pushButton.setIcon(self.icone_plutao)
        self.ui.pushButton.clicked.connect(self.clicando)
        self.ui.pushButton.clicked.connect(self.contar_pontos)
        self.ui.pushButton_mercurio.clicked.connect(lambda: self.alterar_imagem("mercurio"))
        self.ui.pushButton_venus.clicked.connect(lambda: self.alterar_imagem("venus"))
        self.ui.pushButton_mars.clicked.connect(lambda: self.alterar_imagem("marte"))
        self.ui.pushButton_terra.clicked.connect(lambda: self.alterar_imagem("terra"))
        self.ui.pushButton_netuno.clicked.connect(lambda: self.alterar_imagem("netuno"))
        self.ui.pushButton_urano.clicked.connect(lambda: self.alterar_imagem("urano"))
        self.ui.pushButton_saturno.clicked.connect(lambda: self.alterar_imagem("saturno"))
        self.ui.pushButton_jupiter.clicked.connect(lambda: self.alterar_imagem("jupiter"))
        self.ui.pushButton_bigbang.clicked.connect(self.resetar)
        
        self.pontos=0       
          
        self.precos = {
        "mercurio": 100,
        "venus": 500,
        "marte": 1000,
        "terra": 1100,
        "netuno": 1200,
        "urano": 1500,
        "saturno": 2000,
        "jupiter": 2500
        }



       

    def resetar(self):
        self.ui.label_2.clear()
        self.pontos =0
       
       
       
 
    def clicando(self):
        self.ui.pushButton.setIconSize(QSize(100,100))
        QTimer.singleShot(100, lambda: self.ui.pushButton.setIconSize(QSize(200, 200)))
   
    def contar_pontos(self):
        if self.ui.pushButton.icon().cacheKey() == self.icone_plutao.cacheKey():
            self.pontos+=1
            self.ui.label_2.setText(f"Pontos: {self.pontos}")
            
 
        elif self.ui.pushButton.icon().cacheKey() == self.icone_mercurio.cacheKey():
            self.pontos+=2
            self.ui.label_2.setText(f"Pontos: {self.pontos}")
            return self.pontos
        
 
        elif self.ui.pushButton.icon().cacheKey() == self.icone_marte.cacheKey():
            self.pontos+=5
            self.ui.label_2.setText(f"Pontos: {self.pontos}")
            return self.pontos
 
        elif self.ui.pushButton.icon().cacheKey() == self.icone_venus.cacheKey():
            self.pontos+=10
            self.ui.label_2.setText(f"Pontos: {self.pontos}")
            return self.pontos
 
        elif self.ui.pushButton.icon().cacheKey() == self.icone_terra.cacheKey():
            self.pontos+=20
            self.ui.label_2.setText(f"Pontos: {self.pontos}")
            return self.pontos
 
        elif self.ui.pushButton.icon().cacheKey() == self.icone_netuno.cacheKey():
            self.pontos+=50
            self.ui.label_2.setText(f"Pontos: {self.pontos}")
            return self.pontos
 
        elif self.ui.pushButton.icon().cacheKey() == self.icone_urano.cacheKey():
            self.pontos+=100
            self.ui.label_2.setText(f"Pontos: {self.pontos}")
            return self.pontos
 
        elif self.ui.pushButton.icon().cacheKey() == self.icone_saturno.cacheKey():
            self.pontos+=150
            self.ui.label_2.setText(f"Pontos: {self.pontos}")
            self.pontos
 
        elif self.ui.pushButton.icon().cacheKey() == self.icone_jupiter.cacheKey():
            self.pontos+=200
            self.ui.label_2.setText(f"Pontos: {self.pontos}")
            return self.pontos

    def alterar_imagem(self,nomes):
        caminho = {
        "mercurio": self.icone_mercurio,
        "venus": self.icone_venus,
        "marte": self.icone_marte,
        "terra": self.icone_terra,
        "netuno": self.icone_netuno,
        "urano": self.icone_urano,
        "saturno": self.icone_saturno,
        "jupiter": self.icone_jupiter,


        }

        if nomes in caminho:
             
            preco = self.precos.get(nomes, 0)  

            if self.pontos >= preco:
                    self.pontos -= preco 
                    self.ui.pushButton.setIcon(caminho[nomes]) 
                    self.ui.pushButton.setIconSize(QSize(200, 200))
                    self.ui.label_2.setText(f"Pontos: {self.pontos}")
            else:
                QMessageBox.warning(self, "Pontos insuficientes", f"Você precisa de {preco} pontos para trocar para {nomes.title()}!")

        else:
            print(f"imagem para {nomes} nao encontrado")






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())