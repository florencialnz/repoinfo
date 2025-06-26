def promedio(notas):
    return sum(notas) / len(notas)
promedio_flor = promedio([6, 8, 10, 9, 6])
promedio_pablo = promedio([7, 10, 9, 5, 8])


print(f"Promedio de Flor: {promedio_flor}")
print(f"Promedio de Pablo: {promedio_pablo}")

# *args permitepasar un numero variable de argumentos a una funcion

def suma(*numeros):
    resultado = 0
    for n in numeros:
        resultado += n
    return resultado

resultado = suma(4, 8, 15)
print(f"Resultado: {resultado}")

    