nombre = "Flor"
edad = 29
saludo = "Hola me llamo {} y tengo {} años".format(nombre,edad)
print(saludo)
saludo = f"Hola me llamo {nombre} y tengo {edad} años"
print(saludo)
#concatenacion de strings#
cadena1= "Hola"
cadena2= "mundo"
cadena_concatenada= cadena1 + " " + cadena2
print(cadena_concatenada)

cadena_repetida = cadena2 * 6
print(cadena_repetida)

cadena= "Hola mundo"
longitud = len(cadena)
print(longitud)
# Alt 92 para hacer \ #
cadena= "Hola mundo"
subcadena = cadena[0:6]
print(subcadena)

cadena_invertida = cadena[::-1]
print(cadena_invertida)

cadena_mayuscula = cadena.upper()
print(cadena_mayuscula)

cadena_minuscula = cadena.lower()
print(cadena_minuscula)

cadena_capitalize = cadena.capitalize()
print(cadena_capitalize)

cadena_reemplazo = cadena.replace("Hola", "algo")
print(cadena_reemplazo)

