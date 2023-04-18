

# Buscar LINEAL o SECUENCIA: si un número existe en la lista
def busqueda_secuencial (lista_numeros,num):
    # for i in range(0,len(lista_numeros)): => esta esta bien, pero es mas rapido lo de abajo.
    encontrado = False

    for _numero in lista_numeros:
        if num == _numero:
            encontrado = True
            break  # => una vez encontrado sale del bucle para no recorrer toda la lista al pedo.
    
    return encontrado

# Buscar LINEAL o SECUENCIAL: si un número existe en la lista y si es así devuelve 
# la posición dentro de la misa
def busqueda_secuencial_indice (lista_numeros,num):
    # for i in range(0,len(lista_numeros)): => esta esta bien, pero es mas rapido lo de abajo.
    encontrado = False
    posicion = -1

    for indice in range(0,len(lista_numeros)):
        if num == lista_numeros[indice]:
            encontrado = True
            posicion = indice + 1
            break  # => una vez encontrado sale del bucle para no recorrer toda la lista al pedo.
    
    return encontrado, posicion

# Busqueda Binaria




lista_numeros = [ 100, 2, 8, 3 , 4 , 55 , 6, 7, 8, 9, 10]


# Buscar secuencialmente o linealmente
while True:

    num = int(input("ingrese un numero de la lista: "))

    encontrado, posicion = busqueda_secuencial_indice(lista_numeros,num)

    if encontrado==True:
        print("Felicidades, el númrero " + str(num) +  " se encontró en la posición " +  str(posicion) + " de la lista")
        break
    else:
        print("Intentalo de nuevo")


# Busqueda binaria


# BUSQUEDA BINARIA 
# pasos:
#       1) Ordenar la lista: ES OBLIGATORIO
#       2) Correr el algorimo de búsqueda binaria


def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos
