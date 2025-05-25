a = 10
b = 3

resultado = a
print(f"Operador =: {resultado}")

# a = a + b
a += b
print(f"Operador +=: {a}")

a = 10
# a = a - b
a -= b
print(f"Operador -=: {a}")

lista_1 = [1, 2, 3] 
lista_2 = [4, 5] 
# lista_1 = lista_1 + lista_2
lista_1 += lista_2

print(f"Operador +=: {lista_1}")

a = 10
b = 3

print(f"Operador ==: {a == b}")
print(f"Operador is: {a is b}")

x = "hola"
y = "hola"

print(f"Operador ==: {x == y}")
print(f"Operador is: {x is y}")

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

print(f"Operador ==: {lista1 == lista2}")
print(f"Operador is: {lista1 is lista2}")

resultado = a != b
print(f"Operador !=: {resultado}")

resultado = a > b
print(f"Operador >: {resultado}")

resultado = a < b
print(f"Operador <: {resultado}")


resultado = a >= b
print(f"Operador >=: {resultado}")

resultado = a <= b
print(f"Operador <=: {resultado}")

a = 10
b = 3
c = 20

# AND
resultado = a > b and a < c
print(f"Operador and: {resultado}")

# OR
resultado = a > 20 or a < 5
print(f"Operador or: {resultado}")

# NOT
resultado = not a > b
print(f"Operador not: {resultado}")

a = 10
b = 3
texto = "Hola mundo"
lista = [1, 2, 3, 4, 5]

# IN
resultado = "mundo" in texto
print(f"Operador in: {resultado}")

resultado = 6 in lista
print(f"Operador in: {resultado}")

resultado = 6 not in lista
print(f"Operador in: {resultado}")

a = 1
b = 3

resultado = "a es mayor que b" if a > b else "b es mayor que a"
print(f"Operador ternario: {resultado}")