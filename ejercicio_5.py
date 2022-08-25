# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# --------------------------------
# Aquí copiar la función "generar_invitados"
# ya elaborada
def generar_invitados(cantidad):
    lista_invitados = []
    for i in range(cantidad):
        print("Ingrese el invitado nº ", i+1)
        nombre_invitado = input()
        lista_invitados.append(nombre_invitado)
    return lista_invitados
# --------------------------------

# --------------------------------
# Aquí copiar la función "ordenar"
# ya elaborada
def ordenar(lista):
    ordenada = sorted(lista)
    return ordenada


def imprimir_invitados(lista_invitados):
    print("Los invitados son:")
    for i in range(len(lista_invitados)):
        print(lista_invitados[i])

# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # Alumno: Copiar las funciones "generar_invitados" y "ordenar"
    # creadas en los ejercicios anteriores
    # Deberá copiarlas fuera del bucle "__main__" como se detalla
    # al comienzo del archivo
    # --> El objetivo es generar una lista de invitados y ordenala

    # Luego de copiar las funciones, invocarla en este lugar:

    # 1) Primero generar una lista de invitados con "generar_invitados"
    #    Almacenar el resultado en "lista_invitados"

    # lista_invitados = generar_invitados()
 while True:
        cantidad_invitados = input("Ingrese la cantidad de invitados: ")
        if cantidad_invitados.isdigit():
            cantidad_invitados = int(cantidad_invitados)
            if cantidad_invitados > 0:
                break
            else:
                print("entrada erronea")
        else:
            print("entrada erronea")

lista_invitados = generar_invitados(cantidad_invitados)
    # 2) Luego ordenar la lista de invitados con "ordenar"
    #    --> Pasar como parámetro la "lista_invitados"
    #    --> Retornar la lista de invitados ordenada

    # lista_invidatos_ordenada = ordenar(lista_invitados)
 lista_invidatos_ordenada = ordenar(lista_invitados)
    # Imprimir en pantalla "lista_invidatos_ordenada":
 imprimir_invitados(lista_invidatos_ordenada)
    print("terminamos")
