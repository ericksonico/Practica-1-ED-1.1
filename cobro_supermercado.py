n = int(input('¿Cuántos productos comprarás? '))
productos = [] #Arreglo para guardar los productos
precios = []  #Arreglo para guardar los precios
lista_auxiliar = [] #lista que guarda los precios y los productos en ese orden para poder ordenarlos
lista_final = [] #Lista que guarda los productos y los precios
total = 0 #variable para guardar el total de la compra


i = 0
while i < n:
    producto = input('Producto ' + str(i+1) + ' ')
    productos.append(producto)
    precio = input('Precio del producto ' + str(i+1) + ' $')
    precios.append(float(precio))
    print('\n')
    i = i + 1

for precio in precios:
    total += precio


j= 0
while j < n:
    elemento_lista = [precios[j], productos[j]]
    lista_auxiliar.append(elemento_lista)
    j = j + 1

lista_auxiliar.sort(reverse = True)

print('\n ********************** \n')

k = 0
while k < n:
    lista_elemento_aux = (str(k+1) + ' | ' + str(lista_auxiliar[k][1]) + ' | $' + str(lista_auxiliar[k][0]))
    lista_final.append(lista_elemento_aux)
    k = k +1    

for elemento in lista_final:
    print(elemento)

print(" \n El total es de: $" + str(total))