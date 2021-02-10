import random

# def es_correcto(numero):


def run():
    aleatorio = random.randint(1,100)
    numero = int(input("Hola bienvenido, adivina el número del 1 al 100 en que estoy pensando: "))
    #vidas = 5
    #if vidas > 0:
    while numero != aleatorio:
        vidas = 5
        #if vidas > 0:
            #vidas = 5
        if numero > aleatorio:
            #vidas -= 1
            numero = int(input("Ese no es el número que pensé, intenta con un número más chico: "))        
            #vidas -= 1
        else:
            #vidas -= 1
            numero = int(input("Ese no es el número que pensé, intenta con un número más grande: "))
            #vidas -= 1
        #return vidas
        #else:
        #    print ("Perdiste, ya no te quedan vidas :( ")               
    print ("¡Ese es el número, ganaste!")
    #else:
        #print ("Perdiste, ya no te quedan vidas :( ")
        
if __name__ == '__main__' :
    run()