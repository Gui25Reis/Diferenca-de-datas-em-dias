######    Gui Reis   -   guisreis25@gmail.com    ######    COPYRIGHT © 2020 KINGS

# -*- coding: utf-8 -*-

## Classe responsável pela criação da janela home

#    Nessa classe é criada a página de início do programa e também onde acontece qualquer 
# alteração dentro dela. É importante ressaltar que não está sendo usado o encapsulamento
# direto da POO. Em Python o ancapsulamento funciona de uma forma diferenciada.


## Bibliotecas necessárias:
# Arquivo local:
from dif_emDias import Dif_emDias as difD
from languages import Language

# GUI:
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont


class Gui_home(QtWidgets.QWidget):
    ## Construtor: define a super classe e também a janela principal
    def __init__(self) -> None:                                 
        super(Gui_home, self).__init__()

        self.lg = Language()                                                    # Instancia a classe das linguagens
        self.txts = self.lg.getList(1, 1)                                       # Atributo para guardar os texto usados na GUI
        
        self.res = ''                                                           # Atributo que guarda o texto mostrado ao usuário
        self.calculo = difD()

        self.gui_Ui()                                                           # Chama o método de construção da GUI (Interface Gráfica)
        self.clearResult()                                                      # Define as datas e o texto de saída como padrão


    ## Destruidor: desaloca os atributos declarados
    def __del__(self) -> None:
        del self.txts, self.res, 
        del self.lg, self.calculo                                               # Deleta os objetos instanciados + atributos


    ## Método: cria e configura a janela
    def gui_Ui(self) -> None:
    ## -----------------------------------------------------------------------------------------------
    ## Data inicial e final:
        self.lb_Inicial = self.lbl(self.txts[0], 11, 20, 10, 111, 21, self)     # Cria a label com as coordenadas
        self.dt_Inicial = self.dta(20, 30, 110, 22, self)                       # Cria a entrada (data) com as coordenadas

        self.lb_Final = self.lbl(self.txts[1], 11, 150, 10, 111, 21, self)      # Cria a label com as coordenadas
        self.dt_Final = self.dta(150, 30, 110, 22, self)                        # Cria a entrada (data) com as coordenadas


    ## ------------------------------------------------------------------------------------------------
    ## Cálculo e resultado:
        self.bt_Ok = QtWidgets.QPushButton("OK", self)                          # Cria o botão
        self.bt_Ok.setGeometry(QtCore.QRect(181, 110, 80, 25))                  # Define a posição
        self.bt_Ok.setFont(QFont('Arial', 10))                                  # Define a fonte         

        self.lb_Resposta = QtWidgets.QTextBrowser(self)                         # Cria o campo de resposta
        self.lb_Resposta.setGeometry(QtCore.QRect(20, 60, 240, 40))             # Define a posição
        self.lb_Resposta.setFont(QFont('Arial', 10))                            # Define a fonte         
        
    ## ------------------------------------------------------------------------------------------------
    ## Copyright + Versão:
        txt_Copyright = "COPYRIGHT © 2020 KINGS"                                # Texto copyright (MIT License)
        copyright_Txt = self.lbl(txt_Copyright, 6, 10, 120, 120, 16, self)      # Cria a lbl com as coordenadas
        copyright_Txt.setFont(QFont('Arial', 6, QFont.Bold))                    # Define a fonte

        txt_Version = "V 1.0 (12/20)"                                           # Texto da versão
        version_Txt = self.lbl(txt_Version, 6, 7, 109, 71, 16, self)            # Cria a lbl com as coordenadas
        version_Txt.setFont(QFont('Arial' ,6, QFont.Bold))                      # Define a fonte


## ------------------------------------------------------------------------------------------------
## ------------------------------------------------------------------------------------------------
### Funções gerais:

    ## Método: Cria todas as lbls
    def lbl(self, txt_, tam_, p1_, p2_, p3_, p4_, wid_) -> QtWidgets.QLabel:
        lb = QtWidgets.QLabel(txt_, wid_)                                       # Cria uma label
        lb.setGeometry(QtCore.QRect(p1_, p2_, p3_, p4_))                        # Define a posição
        lb.setFont(QFont('Arial', tam_))                                        # Define a fonte
        lb.setAlignment(QtCore.Qt.AlignCenter)                                  # Define o alinhamento
        return lb

    ## Método: Cria as datas
    def dta (self, p1_, p2_, p3_, p4_, self_) -> QtWidgets.QDateEdit:
        data = QtWidgets.QDateEdit(self_)                                       # Cria uma data (caixa de entrada)
        data.setGeometry(QtCore.QRect(p1_, p2_, p3_, p4_))                      # Define a posição
        data.setAlignment(QtCore.Qt.AlignCenter)                                # Define o alinhamento
        data.setFont(QFont('Arial', 11))                                        # Define a fonte
        data.setCalendarPopup(True)                                             # Add o botão para um calendário pop-up
        data.calendarWidget().setFont(QFont('Arial', 8))                        # Define a fonte do pop-up
        data.calendarWidget().setGridVisible(True)                              # Define as linhas do pop-up
        return data

## ------------------------------------------------------------------------------------------------
## ------------------------------------------------------------------------------------------------
### Outros métodos:

    ## Método: faz o cálculo dos dias entre as datas
    def ok_Action(self, dtFormat_:str) -> None:
        dI = self.format_Date(str(self.dt_Inicial.date().toPyDate()), dtFormat_)    # Pega as datas inseridas e transforma em data para python
        dF = self.format_Date(str(self.dt_Final.date().toPyDate()), dtFormat_)
        
        self.calculo.setDatas(self.fix_Date(self.dt_Inicial), 
                              self.fix_Date(self.dt_Final))                         # Define as datas para o cálculo
        if (self.calculo.is_possible()):                                            # Verifica se eh possivel fazer o cálculo
            self.res = str(self.txts[4](dI, dF, self.calculo.result())) + self.res  # Adiciona o resultado
            self.fix_bkColor(255)                                                   # Define a cor de fundo: branco
        else:
            self.res = (str(self.txts[3] + self.res))                               # Mostra a mensagem de erro
            self.fix_bkColor(175)                                                   # Define a cor de fundo: vermelho

        self.lb_Resposta.setText(self.res)                                          # Mostra o resultado ao usuário


    ## Método: Arruma a data de (aaaa-mm-dd) para (dd/mm/aaaa)
    def fix_Date(self, dt_:QtWidgets.QDateEdit) -> str:
        aux = QtWidgets.QDateEdit()                                             # Varíavel auxiliar: copia a data
        aux.setDate(dt_.date())                                                 # Define a mesma data
        aux.setDisplayFormat("dd/MM/yyyy")                                      # Deixa a auxliar como data normal
        s = str(aux.date().toPyDate())                                          # Deixa em formato para python
        del aux                                                                 # Deleta o aux (não precisa mais dele)
        return self.format_Date(s, "dd/MM/yyyy")                                # Mostra a data formatada no padrão brasileiro
     

    ## Método: Arruma a data conforme a preferência exigida
    def format_Date(self, s_:str, dt_:str) -> str:
        if (dt_ == "MM/dd/yyyy"):                                               # Opc: MM/dd/yyyy
            aux = s_.split("-")[::-1]                                           # Cria uma lista invertida com cada parte da data
            aux.insert(0, aux.pop(1))                                           # Troca de posição o mês com o dia
            return "/".join(aux)                                                # Troca o "-" por "/"
        elif (dt_ == "yyyy/MM/dd"):                                             # Opc: yyyy/MM/dd
            return s_.replace("-","/")                                          # Apenas troca o "-" por "/"
        return "/".join(reversed(s_.split("-")))                                # Inverte a lista e troca o "-" por "/"    


    ## Método: Muda o fundo das entradas
    def fix_bkColor(self, c_:int) -> None:
        self.dt_Inicial.setStyleSheet(f"QDateEdit {{background-color: rgb(255, {c_}, {c_});}}") # Muda a cor de fundo
        self.dt_Final.setStyleSheet(f"QDateEdit {{background-color: rgb(255, {c_}, {c_});}}")   

 
    ## Método: Muda o formato da data
    def setDateFormat(self, s_:str) -> None:
        self.dt_Inicial.setDisplayFormat(s_)                                 # Muda o formato das datas
        self.dt_Final.setDisplayFormat(s_)


    ## Método: limpa o resultado.
    def clearResult(self) -> None:
        self.dt_Inicial.setDate(QtCore.QDate(2000, 11, 4))                      # Padrão inicial: meu aniversário
        self.dt_Final.setDate(QtCore.QDate.currentDate())                       # Padrão final: data do momento

        self.res = self.txts[2]                                                 # Limpa a variável
        self.lb_Resposta.setText(self.res)                                      # Coloca a variável limpa
        self.fix_bkColor(255)                                                   # Muda a cor pra branco (caso esteja vermelho)
    

    ## Método especial: Define a linguagem
    def setLanguage(self, type_:int) -> None:
        self.txts = self.lg.getList(type_, 1)                                   # Define a lista com os textos na liguagem pedida
        self.translate()
    

    ## Método: Muda a lingusgem
    def translate(self) -> None:
        self.lb_Inicial.setText(self.txts[0])                                   # Data inicial
        self.lb_Final.setText(self.txts[1])                                     # Data final