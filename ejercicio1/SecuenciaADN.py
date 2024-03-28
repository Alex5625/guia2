

class Secuencia():
    
    def __init__(self):

        self.__identificador = None
        self.__secuencia = None
        self.__especie = None

    def set_iniciar_datos(self,identificador,secuencia,especie):
        
        self.__identificador = identificador
        self.__secuencia = secuencia
        self.__especie = especie

        pass


    def get_nambre(self):
        return f"{self.__identificador}, {self.__secuencia}, {self.__especie}"
    
    def get_largo_secuencia(self):
        return f"El largo de la secuencia es: {len(self.__secuencia)}"
    
    def set_modificaADN_en_ARN(self):
        palabra = ""
        for i in range(len(self.__secuencia)):
            letra = self.__secuencia[i]
            if letra == "T":
                letra = "U"
            palabra = palabra + letra
            # print(palabra)

        self.__secuencia = palabra

    

    

