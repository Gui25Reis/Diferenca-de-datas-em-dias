def Dias_nos_Meses(variavel_):
    global dias_meses
    
    if variavel_ == 2:
        dias_meses += 28
    
    elif variavel_ in meses31_30[0]:                                                                                         #comparando as variáveis
        dias_meses += 31                                                                                                                            

    elif variavel_ in meses31_30[1]:
        dias_meses += 30

meses31_30 = [[1,3,5,7,8,10,12] , [2,4,6,9,1]]
meses = [1,2,3,4,5,6,7,8,9,10,11,12] 

anos_bissextos = 0
dias_meses = 0  

# Data de Inicial:
data_inicial = input('Digite a data inicial (dd/mm/aaaa): '). split('/')                                                                                                         #Seprando as varáveis em dia, mês e ano 

dia_inicial = int(data_inicial[0])                                                                                                                                                                            #Defindo que os valores são inteiros (str -> int)                                
mes_inicial = int(data_inicial[1])
ano_inicial = int(data_inicial[2])

# Data Final:
data_final = input('Digite a data final (dd/mm/aaaa): '). split('/')

dia_final = int(data_final[0])
mes_final = int(data_final[1])
ano_final = int(data_final[2])

#Cálculo: idade/anos completos:
if (mes_final > mes_inicial) or (mes_final == mes_inicial and dia_final >= dia_inicial):                                                                                                                                             #Se os dias forem iguais ou maiores subtrai os anos      
    idade = ano_final - ano_inicial    
else:
    idade = ano_final - ano_inicial  - 1                                                                                                                                                              #Se os dias nã0 forem iguais, tira 1 (ainda não chegou no aniversário, não completou 1 ano ainda)                                          

#Anos bissextos:
for inter_anos in range(ano_inicial, ano_final + 1):                                                                                                                                                  #Acha os anos completos que passaram                    
    if (inter_anos%400 == 0 and inter_anos%4 == 0) or (inter_anos%100 != 0 and inter_anos%4 == 0):                                                                                                    #Compara os anos com a regra para ser ano bissexto                                            
        anos_bissextos += 1

    if mes_inicial >= 2 and ano_inicial == inter_anos:                                                                                                                                            #Se o mes inicial for jan ou fev ou ano final for acima de fev (ja passou o dia extra) conta o ano inicial como bissexto                                            
        anos_bissextos -= 1

#Cálculo: dias restantes:
if mes_final == mes_inicial:                                                                                                                                                                          #Se os meses forem iguais a conta fica mais fácil                                                                        
    if dia_inicial > dia_final:
        dias_meses = 365 - (dia_inicial - dia_final)                                                                                                                 #Dias que faltam para completar o ano                                           
    else:
        dias_meses = dia_final - dia_inicial                                                                                                                #Dias que passaram do ano q acabo de ser completado


elif mes_final > mes_inicial:

    if mes_inicial + 1 == mes_final:
        Dias_nos_Meses(mes_inicial)
    else:
        for mes_interv in range(mes_inicial, mes_final):                                                                                                                                          #Meses que passaram do último aniversário                                                            
            Dias_nos_Meses(mes_interv)
    
    dias_meses += (dia_final-dia_inicial)


elif mes_final < mes_inicial:                                                                                                                                                                  #meses: 01-Jan, 02-Fev ... 12-Dez
    for meses_faltam in range(mes_final, mes_inicial):                                                                                                                                 #começa do mes em que estamos e vai até o próximo mes do aniversário                                                                                                                                                #guarda os números numa lista                                                    
        Dias_nos_Meses(meses_faltam)

    dias_meses += (dia_inicial-dia_final) - 365

conta_final = (idade*365) + dias_meses + anos_bissextos

print('Nesse período tiveram:',conta_final,'dias (completos).')