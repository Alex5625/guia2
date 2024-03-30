

class Secuencia():
    
    def __init__(self):

        self.__identificador = None
        self.__secuencia = None
        self.__especie = None

    def set_iniciar_datos(self,arreglo):
    
        self.__identificador = arreglo[0]
        self.__secuencia = arreglo[1]
        self.__especie = arreglo[2]

        pass


    def get_nambre(self):
        return f"{self.__identificador}, {self.__secuencia}, {self.__especie}"
    
    def get_largo_secuencia(self):
        return f"El largo de la secuencia es: {len(self.__secuencia)}"
    
    def set_modificaADN_en_ARN(self):
        palabra = ""
        for i in range(len(self.__secuencia)):
            letra = self.__secuencia[i]
            
            #es entregar la hebra complementaria de adn por como funciona la transcripcion
            if letra == "T":
                letra = "A"

            elif letra == "A":
                letra = "U"

            elif letra == "C":
                letra = "G"

            elif letra == "G":
                letra = "C"

            palabra = palabra + letra
            # print(palabra)

        self.__secuencia = palabra

    

    

