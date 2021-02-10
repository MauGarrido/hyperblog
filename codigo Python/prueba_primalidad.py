def es_primo(numero):
    contador = 0 #En efecto y como su nombre lo dice, cuenta las veces en que encuentra un número por el que se es divisible entre 0 que no sea 1 ni el mismo número
    
    for i in range (1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False



def run():
    numero = int(input("Hola, bienvenido, escribe un número: "))
    if es_primo(numero):
        print("Este es un número primo")
    else:
        print("Este número no es primo")

if __name__ == '__main__':
    run()