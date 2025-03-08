#Lista inicial con sus respectivos datos
miLista =[34, 12, 45, 67, 23, 89, 5, 90, 56, 78]

#Funcion para ordenar la lista de menor a mayor
def operarLista(lista):
    listaOrdenada = sorted(lista)
    print("Lista ordenada", listaOrdenada)

    #Funcion para buscar un elemento en la lista
    subLista = listaOrdenada[2:7]
    print("Sublista (indices 2 al 6):", subLista)

    #Funcion para elevar al cuadrado los elementos de la lista
    nuevaLista = [x**2 for x in subLista]
    print("Nueva lista con elementos elevados al cuadrado:", nuevaLista)

    #Para saber si un elemento esta en la lista
    listaModificada = lista.copy()
    listaModificada[2] = 100
    print("Lista modificada:", listaModificada)

    return listaOrdenada, subLista, nuevaLista, listaModificada
ordenada, sub, nueva, modificada, = operarLista(miLista)    