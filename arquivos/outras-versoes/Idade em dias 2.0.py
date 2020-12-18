def dif_dias(mes_maior_, dia_maior_, mes_menor_, dia_menor_):   # Função: calcula os dias restantes
    d = 0                                                       # Variavel para retorno
    for m in range(mes_menor_+1, mes_maior_):                   # Pega o intervalo de meses entre as datas
        d += mes[m]                                             # Soma eles
    d += (mes[mes_menor_]-dia_menor_) + dia_maior_              # Soma os dias restantes (dos prórpios meses)
    return d

#         jan,fev,mar,abr,mai,jun,jul,ago,set,out,nov,dez
mes = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]             # O zero no início eh para iguala a posição com o npumero do mês

# Data de Inicial:
data_inicial = input('Digite a data inicial (dd/mm/aaaa): '). split('/')

dia_inicial = int(data_inicial[0])
mes_inicial = int(data_inicial[1])
ano_inicial = int(data_inicial[2])

# Data Final:
data_final = input('Digite a data final (dd/mm/aaaa): '). split('/')

dia_final = int(data_final[0])
mes_final = int(data_final[1])
ano_final = int(data_final[2])

# Anos bissextos:
anos_bissextos = 0
for inter_anos in range(ano_inicial, ano_final + 1):                                                    # Pega o intervalo de anos
    if (inter_anos%400 == 0 and inter_anos%4 == 0) or (inter_anos%100 != 0 and inter_anos%4 == 0):      # Se for um ano bissexto
        anos_bissextos += 1                                                                             # Soma
        if mes_inicial >= 2 and ano_inicial == inter_anos:                                              # Se o primeiro ano for bissexto e a data for maior q fev
            anos_bissextos -= 1                                                                         # Não conta o ano bissexto

# Cálculo: dias restantes:
dias_meses = 0
if mes_final == mes_inicial:                                                    # No mesmo mes
    dias_meses += abs(dia_inicial - dia_final)                                  # Adiciona a diferença dos dias

elif mes_final > mes_inicial:                                                   # Se passou da data incial        
    dias_meses += dif_dias(mes_final, dia_final, mes_inicial, dia_inicial)      # Soma os dias que passaram

else:                                                                           # Se não passou 
    dias_meses -= dif_dias(mes_inicial, dia_inicial, mes_final, dia_final)      # Tira quanto que falta

conta_final = (ano_final-ano_inicial)*365 + dias_meses + anos_bissextos         # Conta final

print('\nNesse período tiveram:',conta_final,'dias (completos).')