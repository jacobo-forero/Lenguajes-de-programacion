#Lista inicial
miLista =[34, 12, 45, 67, 23, 89, 5, 90, 56, 78]

#Funcion para ordenar la lista
def operarLista(lista):
    listaOrdenada = sorted(lista)
    print("Lista ordenada", listaOrdenada)

    #Para elevar al cuadrado los elementos de la lista
    expLista = [x**2 for x in miLista]
    print("Lista para elevar al cuadrado:", expLista)

    #Para restar los elementos de la lista
    restaLista = [x-2 for x in miLista]
    print("Lista para restar:", restaLista)

    #Para restar los elementos de la lista
    sumaLista = [x+2 for x in miLista]
    print("Lista para sumar:", sumaLista)

    #Para dividir los elementos de la lista
    dividirLista = [x/2 for x in miLista]
    print("Lista para dividir:", dividirLista)

    #Para multiplicar los elementos de la lista
    mulLista = [x*2 for x in miLista]
    print("Lista para multiplicar:", mulLista)
    
    #Return para devolver el resultado de la lista
    return listaOrdenada, expLista, restaLista, sumaLista, dividirLista, mulLista
ordenada = operarLista(miLista)