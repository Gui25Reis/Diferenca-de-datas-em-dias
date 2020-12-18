######    Gui Reis   -   guisreis25@gmail.com    ######    COPYRIGHT © 2020 KINGS

# -*- coding: utf-8 -*-

## Classe responsável pelo dos dias entre duas datas.

class Dif_emDias:
    ## Construtor: define os atributos separando cada índice da data
    def __init__(self) -> None:
        #            jan,fev,mar,abr,mai,jun,jul,ago,set,out,nov,dez
        self.mes = (0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)                           # O zero no início é para igualar a posição com o número do mês    

    ## Destruidor: Deleta os atributos
    def __del__(self) -> None:
        del self.mes
        del self.dia_Ini, self.mes_Ini, self.ano_Ini
        del self.dia_Fin, self.mes_Fin, self.ano_Fin


    ## Método especial: define as datas
    def setDatas(self, dt_Ini_:str, dt_Fin_:str):
        # Data Inicial:
        self.dia_Ini, self.mes_Ini, self.ano_Ini = map(int, dt_Ini_.split("/"))                                 # Cria os atributos

        # Data Final:
        self.dia_Fin, self.mes_Fin, self.ano_Fin = map(int, dt_Fin_.split("/"))


    ## Método: calcula os dias restantes.
    def dif_dias(self, mes_maior_, dia_maior_, mes_menor_, dia_menor_) -> int:
        d = 0                                                                                                   # Variável para retorno
        for m in range(mes_menor_+1, mes_maior_):                                                               # Pega o intervalo de meses entre as datas
            d += self.mes[m]                                                                                    # Soma eles
        d += (self.mes[mes_menor_]-dia_menor_) + dia_maior_                                                     # Soma os dias restantes (dos próprios meses)
        return d


    ## Método: calcula os anos bissextos.
    def bissexto(self) -> int:
        anos_bi = 0
        for inter_anos in range(self.ano_Ini, self.ano_Fin + 1):                                                # Pega o intervalo de anos
            if (inter_anos%400 == 0 and inter_anos%4 == 0) or (inter_anos%100 != 0 and inter_anos%4 == 0):      # Se for um ano bissexto
                anos_bi += 1                                                                                    # Soma
                if (self.mes_Ini >= 2 and self.ano_Ini == inter_anos):                                          # Se o primeiro ano for bissexto e a data for maior que fevereiro
                    anos_bi -= 1                                                                                # Não conta o ano bissexto
        return anos_bi


    ## Método: verifica se é possível fazer a conta.
    def is_possible(self) -> bool:
        if (self.ano_Ini > self.ano_Fin):
            return False                 
        elif (self.ano_Ini == self.ano_Fin) and (self.mes_Ini > self.mes_Fin):
            return False
        elif (self.ano_Ini == self.ano_Fin) and (self.mes_Ini == self.mes_Fin) and (self.dia_Ini > self.dia_Fin):
            return False
        return True                                                                                             # Eh válido


    ## Método: calcula os dias restantes.
    def result(self) -> int:
        dias_meses = 0
        if (self.mes_Fin == self.mes_Ini):                                                                      # No mesmo mês
            dias_meses += abs(self.dia_Ini - self.dia_Fin)                                                      # Adiciona a diferença dos dias
        elif (self.mes_Fin > self.mes_Ini):                                                                     # Se passou da data incial        
            dias_meses += self.dif_dias(self.mes_Fin, self.dia_Fin, self.mes_Ini, self.dia_Ini)                 # Soma os dias que passaram
        else:                                                                                                   # Se não passou 
            dias_meses -= self.dif_dias(self.mes_Ini, self.dia_Ini, self.mes_Fin, self.dia_Fin)                 # Tira quanto que falta
        return (self.ano_Fin-self.ano_Ini)*365 + dias_meses + self.bissexto()                                   # Conta final