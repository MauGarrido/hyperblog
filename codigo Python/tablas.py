def ciclo(tabla):
        for contador in range (1,11):
            print(contador*tabla)

def run():
    tabla = int(input("""Bienvenido, indica la tabla que quieres visualizar:
    
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
        print (ciclo(tabla))
    else:
        print ("""
    No has elegido una opción de las que te presentamos, go home
        """)
        
if __name__ == '__main__':
    run()