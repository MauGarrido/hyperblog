#def func():
    #print ("ola ke ase?")

#func()
#func()

def conversacion (mensaje):
    print ("Hola")
    print ("¿Cómo estás?")
    print (mensaje)    
    

opcion = int(input("Elige una opción (1, 2, 3) "))
if opcion == 1 :
    conversacion ("Elegiste la opción 1")
elif opcion == 2:
    conversacion ("Elegiste la opción 2")
elif opcion == 3 :
    conversacion ("Elegiste la opción 3")
else:
    print ("Lo siento, elige una opción válida")