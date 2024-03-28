#debo hacer que se alamcenen los datos en un objeto
#usar get y set
#ver la longitud de la secuencia
#modificar la T por la U en la secuencia
from SecuenciaADN import Secuencia

if __name__ == "__main__":

    secuencia1 = Secuencia()

    secuencia1.set_iniciar_datos("SEQ001","ATCGATCGATCGATCGTGTSCT", "HOMO SAPIENS")

    print(secuencia1.get_nambre())
    
    print(secuencia1.get_largo_secuencia())

    secuencia1.set_modificaADN_en_ARN()

    print(F"lA SECUENCIA MODIFICADA ES: {secuencia1.get_nambre()}")