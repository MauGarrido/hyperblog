import random

def generar_contra():
    mayusculas = ["A" , "B", "C", "D", "E", "F", "G"]
    minusculas = ["a", "b", "c", "d", "e", "f", "g"]
    simbolos = ["!", "$", "#", "%", "&", "(", "="]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range (15):
        caracter_random = random.choice(caracteres) # Elije de forma aleatoría de lista caracteres
        contrasena.append(caracter_random)  #Agregar caracter random
    
    contrasena = "".join(contrasena) #El método para convertir la lista en string
    return contrasena  

def run ():
    contrasena = generar_contra()
    print ("Tu nueva contraseña es: " + contrasena)
if __name__ == '__main__':
    run()