from motacion import MutacionGenetica


if __name__ == "__main__":

    genoma = MutacionGenetica()
    genoma.set_inicializar_datos("MUT0001", "SUSTITUCION DE A POR G EN EL GEN ABC",
                                 "GEN ABC", "POSICION 1023-1050","HOMO SAPIENS")
    
    print(genoma.get_entregar_datos())

    if genoma.set_es_puntual():
        print("ESTA SECUENCIA ES PUNTUAL")
    else:
        print("ESTA SECUENCIA NO ES PUNTUAL")