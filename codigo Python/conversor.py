#menu = int(input (""" Bienvenido a tu conversor de monedas, por favor, elije qué moneda quieres convertir a dolares:

#1. Peso Argentino, che
#2. Peso Colombiano, berraco
#3. Peso Mexicano alv

#""))


def conversor (tipo_peso, valor_dolar):
    pesos = int(input ("Genial, introduce la cantidad de pesos " + tipo_peso + " que quieres convertir: "))
    dolares = pesos * valor_dolar
    dolares = round (dolares, 2)
    dolares = str (dolares)
    print ("Tienes $ " + dolares + " Dolares")    
  
menu = int(input (""" Bienvenido a tu conversor de monedas, por favor, elije qué moneda quieres convertir a dolares:

1. Peso Argentino, che
2. Peso Colombiano, parce
3. Peso Mexicano, wey
"""))  

if menu <= 3:
    if menu == 1:
        conversor ("argentinos", 0.011)
    elif menu == 2:
        conversor ("colombianos", 0.00028)
        valor_dolar = 0.00028
    else:
        conversor ("mexicanos", 0.049)
else:
  print("Lo siento, tu moneda no se contempla en nuestra base de datos")



#if menu <= 3:
#    pesos = int(input ("Genial, introduce la cantidad de pesos que quieres convertir: "))
#    if menu == 1:
#        valor_dolar = 0.011
#    elif menu == 2:
#        valor_dolar = 0.00028
#    else:
#        valor_dolar = 0.049
#    dolares = pesos * valor_dolar
#    dolares = round (dolares, 2)
#    dolares = str (dolares)
#    print ("Tienes $ " + dolares + " Dolares")  
#else:
#  print("Lo siento, tu moneda no se contempla en nuestra base de datos")
