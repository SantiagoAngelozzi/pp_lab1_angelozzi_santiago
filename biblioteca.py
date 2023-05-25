import json
import os
#0) funciones reutilizables o complementarias.
def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

def leer_archivo_json(ruta: str) -> list:
    """
    Esta función lee un archivo JSON de una ruta determinada y devuelve una lista de héroes.

    Parametro 
        -ruta:  es una cadena que representa la ruta del archivo JSON que contiene
        los datos a leer

    :return: una lista de jugadores leída de un archivo JSON ubicado en la ruta especificada.

    """
    with open(ruta, "r") as archivo:
        contenido = json.load(archivo)
        lista_jugadores = contenido["jugadores"]
    return lista_jugadores

def imprimir_dato(dato : str):
    '''
    recive un dato tipo str

    imprime el dato 
    '''
    print(dato)

def validar_entero(num) -> bool:
    '''
    recive un numero
    verifica que se un numero
    devuelve un bool
    '''
    return num.isdigit()

def imprimir_menu():
    '''
    imprime el menu
    '''
    imprimir_dato("1) Mostrar la lista de todos los jugadores del Dream Team\n\
                   2) \n\
                   3) \n\
                   4) \n\
                   5) \n\
                   6) \n\
                   7) \n\
                   8) \n\
                   9) \n\
                   10) \n\
                   11) \n\
                   12) \n\
                   13) \n\
                   14) \n\
                   15) \n\
                   16) \n\
                   17) \n\
                   18) \n\
                   19) \n\
                   20)  ")

def dream_team_menu_principal():
    '''
    verifica que sea un numero con la funcion previamente creada
    retorna un numero entero
    '''
    opcion = input("Ingrese una opción: ")
    while not validar_entero(opcion):
        print("Error: debe ingresar un número entero")
        opcion = input("Ingrese una opción: ")
    return int(opcion)

def dream_team_app(jugadores: list):
    '''
    recive una lista
    intercactua con todas la funciones previas

    '''
    while True:
        imprimir_menu()
        opcion = dream_team_menu_principal()
        match opcion:
            case 1:
                mostrar_jugadores(jugadores)
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                pass
            case 11:
                pass
            case 12:
                pass
            case 13:
                pass
            case 14:
                pass
            case 15:
                pass
            case 16:
                pass
            case 17:
                pass
            case 18:
                pass
            case 19:
                pass
            case 20:
                pass
            case _:
                print("Error: opción incorrecta, intente de nuevo")
        clear_console()

# 1) Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
# Nombre Jugador - Posición. Ejemplo:
# Michael Jordan - Escolta 
def mostrar_jugadores(jugadores ):
    if jugadores:
        for jugador in jugadores:
            imprimir_dato(f"{jugador['nombre']} - {jugador['posicion']}")

