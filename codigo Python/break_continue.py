def ciclo(tabla):
    num = int(input("Genial, ahora compártenos el número que más te caiga mal del 1 al 10: "))
    for contador in range (1,11):
            if contador == num:
                continue
            print(contador*tabla)            
    print ("Como te pudiste dar cuenta, no imprimimos el resultado del sucio " + str(num) +" (que es el " + str(num*tabla) + ") en nuestra tabla")

def run():
    # for contador in range(100):
    #     if contador % 2 =/= 0:
    #         continue
    #     print (contador)
    
    # for i in range (100):
    #     print (i)
    #     if i == 68:
    #         break

    # texto = input("Hola escribe un texto:")
    # for letra in texto:
    #     print (letra)
    #     if letra == "o":
    #             break

    tabla = int(input ("""Hola, ingresa la tabla que te gustaría visualizar:
    
    2. Tabla del 2
    3. Tabla del 3
    4. Tabla del 4
    5. Tabla del 5
    6. Tabla del 6
    7. Tabla del 7
    8. Tabla del 8
    9. Tabla del 9
    10.Tabla del 10
    
    """))
       
    if tabla in range (2,11):
        print(ciclo(tabla))
    else:
        print ("No has elegido una opción de las que te presentamos, go home")

    # while nombre > 100:
    #     print (nombre)

if __name__ == '__main__':
    run()