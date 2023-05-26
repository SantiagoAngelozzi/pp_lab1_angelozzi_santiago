import json
import os
import re
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

def guardar_archivo_csv(nombre_archivo: str, contenido: str) -> bool:
    """
    Esta función guarda el contenido de una cadena en un archivo con el nombre de archivo dado y
    devuelve un valor booleano que indica si la operación fue exitosa o no.

    Parametros: 
        -nombre_archivo: Una cadena que representa el nombre del archivo que se va a crear o
        sobrescribir

        -contenido: El contenido que se escribirá en el archivo. Debería ser una cadena

    :retorno: 
        -un valor booleano, ya sea True o False, según si el archivo se creó correctamente o no.
    """

    with open(nombre_archivo, 'w+') as archivo:
        resultado = None
        resultado = archivo.write(contenido)
    if resultado:
        print("Se creó el archivo: {0}".format(nombre_archivo))
        return True

    print("Error al crear el archivo: {0}".format(nombre_archivo))
    return False

def imprimir_dato(dato : str):
    '''
    recive un dato tipo str

    imprime el dato 
    '''
    print(dato)

def imprimir_menu():
    '''
    imprime el menu
    '''
    imprimir_dato("1) Mostrar la lista de todos los jugadores del Dream Team\n2) elije un jugador para mostrar sus estadisticas\n3) elije un jugador para mostrar sus estadisticas y descargarlo en csv \n4) \n5) \n6) \n7) \n8) \n9) \n10) \n11) \n12) \n13) \n14) \n15) \n16) \n17) \n18) \n19) \n20)  ")

def dream_team_menu_principal():
    '''
    verifica que sea un numero con la funcion previamente creada
    retorna un numero entero
    '''
    opcion = input("Seleccione opción: ")
    if re.match(r"^(?:[1-9]|1\d|20)$",opcion):
        opcion = int(opcion)
        return opcion
    else:
        print("Opción inválida. Inténtelo nuevamente")
        return "-1"

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
                seleccionar_jugador(jugadores)
            case 3:
                guardar_estadisticas_csv(jugadores)
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

def mostrar_jugadores(jugadores: list):
    """""
    recive como parametro una lista de jugadores
    recorre la lista  imprime nombre y pocicion de los jugadores
    
    """""
    if jugadores:
        for jugador in jugadores:
            imprimir_dato(f"{jugador['nombre']} - {jugador['posicion']}")

#  2) Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas,
#  incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido, rebotes totales,
#  promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales,
#  bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.

def mostrar_estadisticas_jugador(jugador) -> str:
    """""
    recive un jugador como parametro
    imprime nombre, pocicion y todas las estadisticas
    retorna la lista de estadisticas del jugador
    """""
    dato = f"{jugador['nombre']} - {jugador['posicion']}\
    \nTemporadas jugadas: {jugador['estadisticas']['temporadas']}\
    \nPuntos totales: {jugador['estadisticas']['puntos_totales']}\
    \nPromedio de puntos por partido: {jugador['estadisticas']['promedio_puntos_por_partido']}\
    \nRebotes totales: {jugador['estadisticas']['rebotes_totales']}\
    \nPromedio de rebotes por partido: {jugador['estadisticas']['promedio_rebotes_por_partido']}\
    \nAsistencias totales: {jugador['estadisticas']['asistencias_totales']}\
    \nPromedio de asistencias por partido: {jugador['estadisticas']['promedio_asistencias_por_partido']}\
    \nRobos totales: {jugador['estadisticas']['robos_totales']}\
    \nBloqueos totales: {jugador['estadisticas']['bloqueos_totales']}\
    \nPorcentaje de tiros de campo: {jugador['estadisticas']['porcentaje_tiros_de_campo']}\
    \nPorcentaje de tiros libres: {jugador['estadisticas']['porcentaje_tiros_libres']}\
    \nPorcentaje de tiros triples: {jugador['estadisticas']['porcentaje_tiros_triples']}"
    imprimir_dato(dato)
    return dato
    

def seleccionar_jugador(jugadores: list):
    """""
    recive como parametro una lista de jugadores 
    recorre la lista imprime los jugadores ordenados por indice y da a elejir uno
    """""
    indice = 0
    for jugador in jugadores:
        indice += 1
        print(f"{indice}) {jugador['nombre']}")
    seleccion = int(input("Selecciona un jugador por su índice: "))
    seleccion -= 1
    if seleccion >= 0 and seleccion < len(jugadores):
        jugador = jugadores[seleccion]
        dato = mostrar_estadisticas_jugador(jugador)
    else:
        print("Índice de jugador inválido.")
    return dato
    

# 3) Después de mostrar las estadísticas de un jugador seleccionado por el usuario,
# permite al usuario guardar las estadísticas de ese jugador en un archivo CSV.
# El archivo CSV debe contener los siguientes campos: nombre, posición, temporadas, puntos totales,
# promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, asistencias totales,
# promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo,
# porcentaje de tiros libres y porcentaje de tiros triples.

def guardar_estadisticas_csv(jugadores):
    contenido = seleccionar_jugador(jugadores)
    archivo = "estadisticas_jugador.csv"
    guardar_archivo_csv(archivo, contenido)



    







    
    
    


    

