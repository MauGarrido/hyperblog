import pandas as pd

# Aquí va el código para confirmar si quiere visualizar la información, y en ese caso si quiere cambiarla o simplemente guardarla

def run():
    mi_info = {
    'tarea': input("Hola, bienvenido, guardaremos la tarea quieres registrar, cuál es el nombre de la tarea:"),
    'descripción': input("Genial, danos una breve descripción de ella: "),
    'prioridad': int(input("""Muy bien, ahora ¿cuál es su prioriodad?
    1. Baja
    2. Media
    3. Alta""")),
    'responsable': input("Genial, ya casi terminamos, compártenos un nombre para identificarte dentro de nuestra base de datos: "),
}

df = pd.DataFrame(data, columns = ['tarea', 'descripcion', 'prioridad', 'responsable'])

df.to_excel('datos.xlsx', sheet_name='datos')

if __name__ == '__main__':
    run()