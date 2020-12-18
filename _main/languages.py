######    Gui Reis   -   guisreis25@gmail.com    ######    COPYRIGHT © 2020 KINGS - All rights reserved

# -*- coding: utf-8 -*-

## Classe responsável pelos textos das interfaces gráficas.

## Sobre:
# Para doferenciar cada linguagem, está senod usado variáveis tipo booleano mas em inteiro
#  1 -> Português-Brasil
#  0 -> English

class Language:
    ## Construtor: gera a lista com as palavras
    def __init__(self) -> None:
        self.list = []

    ## Destruidor: apaga a lista criada
    def __del__(self) -> None:
        del self.list

    ## Método: palavras em Português-Brasil
    def pt_br(self, win_:int) -> None:
        if (win_ == 0):     ## gui_main
            self.list = ["Configurações", "Preferências", "Editar", "Limpar tudo",
            ]

        elif (win_ == 1):   ## guiHome
            resp = lambda dI, dF, result: f"De {dI} até {dF} tem {result} dia(s).\n\n"
            self.list = ["Data inicial","Data final","Insira os dados",
                "Data inicial precisa ser menor ou igual que a data final!\n\n",
                resp
            ]
            del resp

        elif (win_ == 2):   ## guiConfig
            self.list = [
                "Configuração", "Idioma", "Geral", "Formato da data",
                "Salvar", "Sair"
            ]

        else:               ## guiPopup
            self.list = ["Confirmação", "Dados não salvo",
                "As alterações não foram salvas, deseja salvar",
                "Sair", "Salvar"
            ]

    ## Método: palavras em English
    def eng(self, win_:int) -> None:
        if (win_ == 0):     ## gui_main
            self.list = ["Settings", "Preferences", "Edit", "Clear",
            ]
            
        elif (win_ == 1):   ## guiHome
            resp = lambda dI, dF, result: f"From {dI} to {dF} you have {result} day(s).\n\n"
            self.list = ["Start date", "End date", "Enter the data",
                "Start date must be less than or equal to the end date!\n\n",
                resp
            ]
            del resp

        elif (win_ == 2):   ## guiConfig
            self.list = [
                "Settings", "Language", "General", "Date format",
                "Save", "Exit"
            ]
        
        else:               ## guiPopup
            self.list = ["Confirmation", "Unsaved data",
                "The changes were not saved, do you want to save?", 
                "Exit", "Save"
            ]
            

    ## Método: retorna a lista coforme a configuração pedida
    def getList(self, lg_:int, win_:int) -> list:
        if (lg_):
            self.pt_br(win_)
        else:
            self.eng(win_)
        return self.list