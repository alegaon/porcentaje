# necesito saber cuanto es el porcentaje de un numero
# datos :
#   %           =   ?
#   total       =   si
#   % cantidad  =   si

# segun clarin
# https://www.clarin.com/sociedad/como-sacar-el-porcentaje-de-un-numero_0_avnnm4TK.html
# 1 mult numero por %
"""
n = 1000
porcentaje = 50 # porciento

def multi_por_porcent(a,b):
    return a*b

paso1 = multi_por_porcent(n, porcentaje)

# 2 dividir resultado por 100
paso2 = paso1 / 100
print(paso2)

# resumiento

resumiendo = (n * porcentaje) / 100
"""
# buscando variables

def total(numero, porcentaje):
    return  (numero * porcentaje) / 100

def numero(total, porcentaje):
    return (total * 100 ) / porcentaje

def porcentaje(numero, total):
    return  numero / (total * 100)

