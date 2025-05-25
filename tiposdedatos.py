edad = 27 #int
print(f"Edad: {edad}, Tipo: {type(edad)}")
      
altura = 1.63 #float
print(f"Altura: {altura}, Tipo:{type(altura)}")
z = 2+5j #complex
print(f"z: {z}, Tipo:{type(z)}")

string = "Flor" #str
print(f"string: {string}, Tipo:{type(string)}")

booleano = True #bool
print(f"booleano: {booleano}, Tipo>{type(booleano)}")

valor = None #nonetype
print(f"valor: {valor}, Tipo:{type(valor)}")

empty_string = ""  # str
print(f"None: {empty_string}, Tipo: {type(empty_string)}")

infinito = float("inf")
print(f"Infinito: {infinito}, Tipo: {type(infinito)}")

nan = float("nan")
print(f"Not a Number: {nan}, Tipo: {type(nan)}")


#listas o arrays son elementos ordenados y mutables
lista = ["algo", 17, 0.5, ["otra lista", True]] # list
print(f"Lista: {lista}, Tipo: {type(lista)}")

#tuplas o tuple son elementos ordenados e inmutables que no pueden cambiar de longitud
tupla = (10.5, 48.5) # tuple
print(f"Tupla: {tupla}, Tipo: {type(tupla)}")

#sets son elementos unicos y no ordenados, no se pueden repetir, si ponemos verde rojo azul verde, el verde no se repite
colores = {"rojo", "verde", "azul"} # set
print(f"Set: {colores}, Tipo: {type(colores)}")

#diccionarios son colecciones o elementos no ordenados, mutables y se accede a ellos por clave (hay que ir tipeando la clave para acceder a su valor y modificarlo)
estudiante = {
  "nombre": "Andres",
  "edad": 29,
  "curso": {
    "nombre": "Programacion web",
    "iniciales": ["PW", "WP"]
  }
}