def regresaMediana (arreglo, longitud):
    return arreglo[longitud//2]

longitud = int(input("Introduce la longitud del arreglo: "))
arreglo = []

for variable in range (longitud):
    elemento = int(input("Ingresa el elemento en la posición " + str(variable) + ": ")) 
    arreglo.append(elemento)

arreglo.sort()

print("****************")

print("La mediana es: " + str(regresaMediana(arreglo, longitud)))
print("Y su índice es: " + str(len(arreglo)//2))