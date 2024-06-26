from motacion import MutacionGenetica
import csv

if __name__ == "__main__":
    contador = 0
    genoma = MutacionGenetica()


    # el parametro de la funcion open es el nombre del archivo
    # siempre es bueno trabajar con una muestra de los datos que representen a la mayor
    # cantidad de posibilidades, en este caso buscar si era o no puntual.
    with open("ejDatos.csv") as rep:
        reader = csv.reader(rep)

        for fila in reader:
            
            if contador != 0:
                genoma.set_inicializar_datos(fila)

                print(genoma.get_entrega_descripcion())
                print(genoma.get_entrega_regionGenomica())
                print(genoma.get_entrega_especie())


    #La manera de encontrar si la mutacion era puntual o no, fue por la posicion del gen en donde sufria la modificacion.
                if genoma.set_es_puntual():
                    print("ESTA SECUENCIA ES PUNTUAL")
                else:
                    print("ESTA SECUENCIA NO ES PUNTUAL")

            contador += 1    
