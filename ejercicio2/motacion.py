
class MutacionGenetica():

    def __init__(self):
        self.__identificador = None
        self.__descripcion = None
        self.__region_genomica = None

        # FALTO AGREGRAR ESTE HEADLINE PARA LOGRAR SEPARAR MEJOR
        self.__posicion = None

        self.__especie = None

    def set_inicializar_datos(self, identificador, descripcion, region_genomica, posicion, especie):

        self.__identificador = identificador
        self.__descripcion = descripcion
        self.__region_genomica = region_genomica
        self.__posicion = posicion
        self.__especie = especie


    def get_entregar_datos(self):
        
        return f"identificador: {self.__identificador} \ndescripcion: {self.__descripcion} \nregion genomica: {self.__region_genomica} \nposicion: {self.__posicion} \nespecie: {self.__especie}"


 #EN EL METODO BUSCAR CON UN CICLO FOR SI TIENE UN (-) NO AFECTA A UN UNICO NUCLEOTIDO
    def set_es_puntual(self):
        letra = True
        for i in range(len(self.__posicion)):
            letra = self.__posicion[i]

            if letra == "-":
                # print("Esta mutacion no es puntual")
                return False
            

