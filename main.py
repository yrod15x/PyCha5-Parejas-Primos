"""Mostrar los numeros primos con una distancia de 2(gemelos), 4(primos) y 6(sexy)"""
from primos import NumPrimos
from random import randint

def mostrar_info(lista, nombre):
    print(f"{nombre} -> {lista}")
    
def extraer_numeros(lista, rango):
    extraidos = []
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] + rango == lista[j]:
                extraidos.append(f"{lista[i]} : {lista[j]}")
    return extraidos
        
primos = NumPrimos(randint(2, 100))
num_primos = primos.generar_num_primos()
print(num_primos)
 
mostrar_info(extraer_numeros(num_primos, 2), "Gemelos")
mostrar_info(extraer_numeros(num_primos, 4), "Primos")
mostrar_info(extraer_numeros(num_primos, 6), "Sexy")