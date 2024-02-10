#Clase que maneja numeros primos mediante la criba de Eratostenes

class NumPrimos:
    def __init__(self, num_limite):
        self.__num_limite = num_limite
        self.__num_primos = []
        
    def generar_num_primos(self)->list:
        """Genera numeros primos usando la criba de Eratostenes. Devuelve una lista de enteros"""
        #Se empieza asumiendo que todos los numeros son primos. Los indices de la lista marcan 
        # los numeros. El 1 y el 0 no son primos
        primos = [True for i in range(self.__num_limite + 1)]
        primos[0], primos[1] = False, False
        
        #Se busca marcar los numeros que sean multiplos (i * j) de numero base (i), esos no serian primos. 
        # La busqueda termina hasta el que el multiplo no sea mayor al cuadrado del numero base.
        i = 2
        while i * i <= self.__num_limite:
            j = i
            while j * i <= self.__num_limite:
                primos[i * j] = False
                j += 1
            i += 1
        
        self.__num_primos = [i for i in range(2, self.__num_limite + 1) if primos[i] == True]
        
        return self.__num_primos