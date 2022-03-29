from email.headerregistry import ContentTransferEncodingHeader


cantidad = int(input('¿Cuántas pelotas hay? '))
limite = int(input('Ingresa el mayor número '))
pelotas = [] #Arreglo del 1 a cantidad
colores = [] #Arreglo que contiene la cantidad de cada color dígito por dígito
resultado = [] #Arreglo donde se almacena la cantidad de pelotas de cada color para imprimir

i = 1
while i <= limite:
    pelotas.append(i)
    i = i+1

print('Ingresa los números de los colores de uno en uno: ')

j = 1
while j <= cantidad:
    color = int(input())
    if color > limite:
        print('Ingresa un número válido')
        if j == 1:
            j = 1
        else:
            j = j-1

    else:
        colores.append(color)
        j = j+1 

k = 1
while k <= limite:
    resultado.append(colores.count(k))
    k = k+1

print('Resultado: ')

l = 0
while l < len(pelotas):
    print(str(pelotas[l]) + ':' + str(resultado[l]))
    l = l + 1