#debo hacer que se alamcenen los datos en un objeto
#usar get y set
#ver la longitud de la secuencia
#USAR SU NUCLEOTIDO COMPLEMENTARIO, ADEMAS SI ES UNA T SU COMPLEMENTRIO
#EN ARN ES U

from SecuenciaADN import Secuencia
import csv

if __name__ == "__main__":
    contador = 0

    secuencia1 = Secuencia()


    #dentro del open() se coloca el nombre del archivo.
    with open("testSecuencia.csv") as per:
        reader = csv.reader(per)

        for fila in reader:
            # print(f"El contador va en: {contador}")
            if contador != 0:
                # print(f"El arreglo es: {fila}")
                # se recorrera el archivo insertando dentro de la clase el arreglo y asi usando los parametros deseados
                secuencia1.set_iniciar_datos(fila)
                print(f"\n{secuencia1.get_nambre()}")
                print(f"{secuencia1.get_largo_secuencia()}")
                secuencia1.set_modificaADN_en_ARN()
                print(f"LA SECUENCIA MODIFICADA ES: {secuencia1.get_nambre()}\n")


            contador += 1

    

