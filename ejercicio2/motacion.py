
class MutacionGenetica():

    def __init__(self):
        self.__identificador = None
        self.__descripcion = None
        self.__region_genomica = None

        # FALTO AGREGRAR ESTE HEADLINE PARA LOGRAR SEPARAR MEJOR
        self.__posicion = None

        self.__especie = None

    def set_inicializar_datos(self, arreglo):

        self.__identificador = arreglo[0]
        self.__descripcion = arreglo[1]
        self.__region_genomica = arreglo[2]
        self.__posicion = arreglo[3]
        self.__especie = arreglo[4]


    def get_entrega_indentificador(self):
        return f"\nidentificador: {self.__identificador}"
        
    def get_entrega_descripcion(self):

        return f"\ndescripcion: {self.__descripcion}" 
    def get_entrega_regionGenomica(self):

        return f"\nregion genomica: {self.__region_genomica}" 
    def get_entrega_posicion(self):

        return f"\nposicion: {self.__posicion}"

    def get_entrega_especie(self):

        return f"\nespecie: {self.__especie}"


 #EN EL METODO BUSCAR CON UN CICLO FOR SI TIENE UN (-) NO AFECTA A UN UNICO NUCLEOTIDO
    def set_es_puntual(self):

        for i in range(len(self.__posicion)):
            letra = self.__posicion[i]
            # print(f"LA LETRA QUE SE VA RECORRIENDO ES: *{letra}*")
            if letra == "-":
                # print("ENTRA EN LA CONDICION")
                # print("Esta mutacion no es puntual")
                return False
            
        return True
            

