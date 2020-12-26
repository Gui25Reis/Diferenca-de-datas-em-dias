######    Gui Reis   -   guisreis25@gmail.com    ######    COPYRIGHT © 2020 KINGS

# -*- coding: utf-8 -*-

## Classe responsável pela criação da janela PopUp

#    Nessa classe é criada a janela Pop-Up quando faz alguma alteração e essa 
# não é salva. Aqui é gerado e feito toda a configuração dela.


## Bibliotecas necessárias:
# Arquivo local:
from languages import Language

# GUI:
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon, QFont

class Gui_popup(QMessageBox):
    ## Construtor: Cria a gui e o necessário para futuras configurações
    def __init__(self) -> None:
        super(Gui_popup, self).__init__()

        self.gui_Ui()                                           # Configura a gui

        self.bt_Cancelar = self.button(self.Cancel)             # Atributo: guarda o botão "Cancel"
        self.bt_Salvar = self.button(self.Save)                 # Atributo: guarda o botão "Save"

        self.lg = Language()                                    # Instancia o objeto para configuração do idioma
        self.setLanguage(1)                                     # Idioma padrão: Português-Brasil

        self.bt_Cancelar.setFont(QFont('Arial', 10))            # Definindo a fonte dos botões
        self.bt_Salvar.setFont(QFont('Arial', 10))

    ## Destruidor: Deleta os atributos
    def __del__(self) -> None:
        del self.lg                                             # Deleta objeto instanciado

    ## Método: Configura a interface (GUI)
    def gui_Ui(self) -> None:
        self.setWindowIcon(QIcon('images/icone.png'))           # Define o icone da janela (geral)
        self.setStyleSheet("QLabel{max-width: 350px;}")         # Define o tamanho máximo do espaço interno
        self.setIcon(self.Question)                             # Define o ícone que mostra ao lado da mensagemm
        self.setStandardButtons(self.Cancel | self.Save)        # Add os botões
        self.setDefaultButton(self.Save)                        # Botão padrão: "salvar"

    ## Método: Mostra a janela.
    def show_PopUp(self) -> int:
        return self.exec()                                      # Executa/Mostra a janela

    ## Método: Retorna o a criação do botão "salvar"        
    def getSave(self) -> QMessageBox.StandardButton:
        return self.Save                                        # Retorna o botão salvar
    
    ## Método: Define a linguagem
    def setLanguage(self, type_:int) -> None:
        self.txts = self.lg.getList(type_, 3)                   # Define a lista com os textos na liguagem pedida
        self.translate()                                        # Faz a mudança do texto

    ## Método: Define/muda o texto
    def translate(self) -> None:
        self.setWindowTitle(self.txts[0])                       # Título da janela
        self.setText(self.txts[1])                              # Tìtulo da mensagem
        self.setInformativeText(self.txts[2])                   # Mensagem (pergunta)
        self.bt_Cancelar.setText(self.txts[3])                  # Botão: cancelar
        self.bt_Salvar.setText(self.txts[4])                    # Botão: salvar