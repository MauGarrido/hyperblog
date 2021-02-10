#potencia = 0
#print("2 elevado a la " + str(potencia) + " es igual a " + str(2**potencia))

def run():
    LIMITE = 1000
    contador = 0
    potencia = 2**contador
    while contador <= LIMITE:
        print("2 elevado a la " + str(contador) + " es igual a " + str(potencia))
        contador = contador + 1
        potencia = 2**contador

if __name__ == '__main__':
    run()