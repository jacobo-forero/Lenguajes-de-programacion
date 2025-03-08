#TABLA DE LA VERDAD

import itertools

def generar_combinaciones(variables):
    #Genera todas las combinaciones de valores booleanos para las variables dadas.
    return list(itertools.product([True, False], repeat=len(variables)))

def imprimir_tabla_verdad(variables):
    #Imprime la tabla de verdad para la operación A y B.
    combinaciones = generar_combinaciones(variables)
    
    # Imprimimos la cabecera de la tabla
    print(f"{' | '.join(variables)} | {' y '.join(variables)}")
    print("-" * (len(variables) * 4 + 10))  # Ajusta el ancho de la línea

    # Evaluamos la expresión para cada combinación
    for combinacion in combinaciones:
        resultado = all(combinacion)  # A y B
        print(" | ".join(map(str, combinacion)) + f" | {resultado}")

def main():
    # Definimos las variables
    variables = ['A', 'B']
    imprimir_tabla_verdad(variables)

# Llamar a la función principal
if __name__ == "__main__":
    main()