def palíndromo (palabra):
        palabra = palabra.replace(" ", "")
        palabra = palabra.lower()
        if palabra == palabra[::-1]:
            return == True


def run():
    palabra = input("""Bienvenido,

Ingresa una palabra: 

""")
    if palíndromo(palabra) == True:
        print("Este es un palíndromo")
    else:
        print("Este no es un palíndromo")



if __name__ == '__main__':
    run()

#palabra = palabra.replace(" ", "")
#palabra = palabra.lower()

#if palabra == palabra[::-1]:
#    print("Esta palabra es un palíndromo")
#else:
#    print("Esta palabra no es un palíndromo")
    