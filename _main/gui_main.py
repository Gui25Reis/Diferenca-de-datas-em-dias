######    Gui Reis   -   guisreis25@gmail.com    ######    COPYRIGHT © 2020 KINGS

# -*- coding: utf-8 -*-

## Classe responsável pela criação da janela princial

#    Aqui é construído a janela principal e também onde junta os outros widgets
# servindo como ponte para as outras três interfaces criadas. Basicamente as ações
# de todos os botões estão sendo feitos por aqui e também as mudanças gerais que
# ocorrem durante o programa.


## Bibliotecas necessárias:
# Arquivo local:
from guiHome import Gui_home
from guiConfig import Gui_config
from guiPopup import *

# GUI:
from PyQt5 import QtCore, QtWidgets


class Gui_main(QtWidgets.QMainWindow):
    ## Construtor: Cria a janela principal com o menu e o local onde vai ser colocado as páginas
    def __init__(self) -> None:
        super(Gui_main, self).__init__()

        self.setWindowIcon(QIcon('images/icone.png'))                   # Define o ícone
        self.setWindowTitle("Diferença em Dias")                        # Define o título da janela
        self.setFixedSize(281, 185)                                     # Sempre vai ser esse tamanho
        
        self.menubar = QtWidgets.QMenuBar(self)                         # Cria a área de menu        
        self.menubar.setGeometry(QtCore.QRect(0, 0, 280, 22))           # Define a sua proporção
        self.setMenuBar(self.menubar)                                   # Define como menu da janela 

        self.root = QtWidgets.QWidget(self)                             # Área principal (root), onde tudo vai ser colocado dentro        
        self.setCentralWidget(self.root)                                # Define como área central

        frame = QtWidgets.QFrame(self.root)                             # Frame: serve como intermediário entre root e o resto dos widgets

        self.allPages = QtWidgets.QStackedWidget(frame)                 # Cria uma área onde armazena vários widgets
        self.allPages.setGeometry(QtCore.QRect(0, 0, 280, 170))         # Define a proporção

        self.home = Gui_home()                                          # Instancia a interface home
        self.allPages.addWidget(self.home)                              # Add na janela

        self.config = Gui_config()                                      # Instancia a interface de configuração
        self.ind_Config = self.allPages.addWidget(self.config)          # Add na janela
        
        self.popup = Gui_popup()                                        # Instancia a interface de PopUp (mensagem)

        self.lg = Language()                                            # Instancia a classe das linguagens (com os textos)
        self.setLanguage(False, 1)                                      # Idioma padrão: Português-Brasil

        self.setNovo()                                                  # Pega as configurações atuais
    
        self.gui_Ui()                                                   # Configura a GUI
    
    
    ## Destruidor: deleta os objetos instanciados
    def __del__(self) -> None:
        del self.home, self.config, self.popup, self.lg                 # Objetos instanciados
        del self.root                                                   # Atributos


    ## Método: configura a interface
    def gui_Ui(self) -> None:
    ## ------------------------------------------------------------------------------------------------
    ## Barra do menu:
        ## Configurações:
        self.mnConfig = QtWidgets.QMenu(self.txts[0], self.menubar)     # Cria o menu de configuração
        self.menubar.addAction(self.mnConfig.menuAction())              # Add na área do menu

        self.actPref = QtWidgets.QAction(self.txts[1], self)            # Cria uma ação
        self.mnConfig.addAction(self.actPref)                           # Add no menu de configuração
        self.actPref.triggered.connect(self.pref_Action)                # Define a sua ação
        
        ## Editar:
        self.mnEditar = QtWidgets.QMenu(self.txts[2] ,self.menubar)     # Cria o menu de editar 
        self.menubar.addAction(self.mnEditar.menuAction())              # Add na área do menu

        self.actLimpar = QtWidgets.QAction(self.txts[3] ,self)          # Cria uma ação
        self.mnEditar.addAction(self.actLimpar)                         # Add no menu de editar
        self.actLimpar.triggered.connect(self.home.clearResult)         # Define a sua ação

    ## ------------------------------------------------------------------------------------------------
    ## Janela: Configuração
        self.config.bt_Sair.clicked.connect(self.sair_Action)           # Define a ação do botão "Sair"

        self.config.bt_Salvar.clicked.connect(self.salvar_Action)       # Define a ação do botão "Salvar"

    ## ------------------------------------------------------------------------------------------------
    ## Janela: Home
        self.home.bt_Ok.clicked.connect(lambda: self.home.ok_Action(self.novo[1]))  # Define a ação do botão "OK"
    

## ------------------------------------------------------------------------------------------------
## ------------------------------------------------------------------------------------------------
### Funções de ação:    
    ## Método: faz a mudança das janelas
    def changeWid(self, h_:bool, wid_:QtWidgets.QWidget) -> None:
        self.allPages.setCurrentWidget(wid_)                            # Muda a página
        self.menubar.setHidden(h_)                                      # Deixa o menu escondido/visível


    ## Método: ação do botão: "preferência" (home)
    def pref_Action(self) -> None:
        self.antes = self.config.getPadrao()                            # Antes de entrar na área de configuração, pega as configurações atuais
        self.changeWid(True, self.config)                               # Muda a tela


    ## Método: ação do botão: "salvar" (configurações)
    def salvar_Action(self) -> None:
        self.setNovo()                                                  # Define as novas configurações

        if (self.novo != self.antes):                                   # Se houve alguma alteração
            if (self.novo[0] != self.antes[0]):                         # Linguagem mudou
                self.setLanguage(True, self.novo[0])                    # Define a nova linguagem    
            if (self.novo[1] != self.antes[1]):                         # Formato da data mudou
                self.home.setDateFormat(self.novo[1])                   # Define o formato das datas
        self.changeWid(False, self.home)                                # Muda a tela
    

    ## Método: ação do botão "sair" (configurações)
    def sair_Action(self) -> None:
        self.setNovo()                                                  # Define as novas configurações

        if (self.novo != self.antes):                                   # Se houve alterção mas não salvou
            conf = self.popup.show_PopUp()                              # Mostra o PopUp (mensagem de aviso)
            if (conf == self.popup.getSave()):                          # PopUp: clicou em salvar
                self.salvar_Action()                                    # Salva as alterações
        self.changeWid(False, self.home)                                # Muda a tela


    ## Método especial: Pega as configurações atuais
    def setNovo(self) -> None:
        self.novo = self.config.getPadrao()                             # Define as novas configurações

        
    ## Método especial: Define a linguagem
    def setLanguage(self, all_:bool, type_:int) -> None:
        self.txts = self.lg.getList(type_, 0)                           # Define a lista com os textos na liguagem pedida
        if all_:                                                        # Se for pra mudar um idioma
            self.translate()                                            # main
            self.home.setLanguage(type_)                                # home
            self.config.setLanguage(type_)                              # config
            self.popup.setLanguage(type_)                               # popup
    

    ## Método: Muda a linguagem
    def translate(self) -> None:
        self.mnConfig.setTitle(self.txts[0])                            # Configuração
        self.actPref.setText(self.txts[1])                              # Preferências
        self.mnEditar.setTitle(self.txts[2])                            # Editar
        self.actLimpar.setText(self.txts[3])                            # Limpar