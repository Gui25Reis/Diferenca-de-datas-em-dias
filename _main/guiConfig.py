######    self Reis   -   guisreis25@gmail.com    ######    COPYRIGHT © 2020 KINGS - All rights reserved

# -*- coding: utf-8 -*-

## Classe responsável pela criação da janela de configuração.

#    Nessa classe é criada a página de configuração do programa, onde faz a alteração
# da idioma e também do formato da data. Todas as configurações da página estão sendo
# feitas aqui.


## Bibliotecas necessárias:
# Arquivos Locais:
from languages import Language

# GUI:
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont


class Gui_config(QtWidgets.QWidget):
    ## Construtor: define a super classe e também a janela config
    def __init__(self) -> None:                                 
        super(Gui_config, self).__init__()
        self.lg = Language()                                                        # Instancia o objeto responsável pelo idioma

        self.txts = self.lg.getList(1, 2)                                           # Idioma padrão: Português-Brazil

        self.gui_Ui()                                                               # Configura a GUI

        self.setPadrao(self.opcLanguage(), self.cBox_Datas.currentText())           # Define as configurações padrões


    ## Destruidor: deleta as varíaveis
    def __del__(self) -> None:
        del self.lg, self.txts                                                      # Deleta o objeto instanciado + atributos
        

    def gui_Ui(self) -> None:
        self.gBox_Config = self.gBox(self.txts[0], 10, 9, 0, 260, 130, self)        # Cria uma grupo (Configurações)

    ## ------------------------------------------------------------------------------------------------
    ## Config - Linguagem:        
        self.gBox_Ling = self.gBox(self.txts[1], 10, 17, 20, 240, 45, self)         # Cria um grupo (Idioma)
        self.gBox_Ling.setFlat(True)                                                # Deixa no modo de uma linha (!= de uma "caixa" [grupo criado acima])
        
        self.rbt_PtBr = QtWidgets.QRadioButton("Português-Brazil", self.gBox_Ling)  # Cria a opção de Idioma
        self.rbt_PtBr.setGeometry(QtCore.QRect(20, 25, 121, 18))                    # Posiciona
        self.rbt_PtBr.setChecked(True)                                              # Deixa marcado como padrão
        
        self.rbg_Eng = QtWidgets.QRadioButton("English", self.gBox_Ling)            # Cria a opção de Idioma
        self.rbg_Eng.setGeometry(QtCore.QRect(160, 25, 61, 18))                     # Posiciona
        

    ## ------------------------------------------------------------------------------------------------
    ## Config - Geral:
        self.gBox_Geral = self.gBox(self.txts[2], 10, 17, 75, 240, 50, self)        # Cria um grupo (Geral)
        self.gBox_Geral.setFlat(True)                                               # Deixa no modo de uma linha (!= de uma "caixa" [grupo criado acima])
        
        self.lbl_Format = QtWidgets.QLabel(self.txts[3], self.gBox_Geral)           # Add uma label
        self.lbl_Format.setGeometry(QtCore.QRect(20, 20, 101, 20))                  # Posiciona
        
        self.cBox_Datas = QtWidgets.QComboBox(self.gBox_Geral)                      # Cria a caixa de opções
        self.cBox_Datas.setGeometry(QtCore.QRect(135, 20, 101, 22))                 # Posiciona
        self.cBox_Datas.addItems(["dd/MM/yyyy", "MM/dd/yyyy", "yyyy/MM/dd"])        # Coloca as opções (padrão: a primeira add [index = 0])

    ## ------------------------------------------------------------------------------------------------
    ## Botões:
        self.bt_Salvar = QtWidgets.QPushButton(self.txts[4], self)                  # Cria o botão 
        self.bt_Salvar.setGeometry(QtCore.QRect(190, 135, 80, 25))                  # Posiciona
        
        self.bt_Sair = QtWidgets.QPushButton(self.txts[5], self)                    # Cria o botão
        self.bt_Sair.setGeometry(QtCore.QRect(100, 135, 80, 25))                    # Posiciona


## ------------------------------------------------------------------------------------------------
## ------------------------------------------------------------------------------------------------
### Funções gerais:
    
    ## Método: Cria todos os "Group Box"
    def gBox(self, txt_, tam_, p1_, p2_, p3_, p4_, wid_) -> QtWidgets.QGroupBox:
        gb = QtWidgets.QGroupBox(txt_, wid_)                                        # Cria uma label
        gb.setGeometry(QtCore.QRect(p1_, p2_, p3_, p4_))                            # Define a posição
        gb.setFont(QFont('Arial', tam_))                                            # Define a fonte
        return gb

    ## Método: Verifica a opção selecionada da linguegem
    def opcLanguage(self) -> bool:
        if self.rbt_PtBr.isChecked():                                               # Verifica se "PortuguÊs-Brazil" está marcado
            return 1                                                                # 1 -> PortuguÊs-Brazil
        return 0                                                                    # 0 -> English

    ## Método especial: Retorna o padrão definido
    def getPadrao(self) -> list:
        return [self.opcLanguage(), self.cBox_Datas.currentText()]                  # Retorna o padrão
        
    ## Método: Define um novo padrão
    def setPadrao(self, lg_:int, fDt_:str) -> None:
        self.lang = lg_                                                             # Define a linguagem
        self.fDate = fDt_                                                           # Define o formato
    
    ## Método: Define a linguagem
    def setLanguage(self, type_:int) -> None:
        self.txts = self.lg.getList(type_, 2)                                      # Define a lista com os textos na liguagem pedida
        self.translate()
    

    ## Método: Muda a linguagem
    def translate(self) -> None:
        self.gBox_Config.setTitle(self.txts[0])                                     # Configuração
        self.gBox_Ling.setTitle(self.txts[1])                                       # Idioma
        self.gBox_Geral.setTitle(self.txts[2])                                      # Geral
        self.lbl_Format.setText(self.txts[3])                                       # Formato da data
        self.bt_Salvar.setText(self.txts[4])                                        # Salvar
        self.bt_Sair.setText(self.txts[5])                                          # Sair