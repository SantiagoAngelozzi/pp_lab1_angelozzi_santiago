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
    with open(ruta, "r", encoding = "utf-8") as archivo:
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
    imprimir_dato("1) Mostrar la lista de todos los jugadores del Dream Team\
    \n2) elije un jugador para mostrar sus estadisticas\
    \n3) elije un jugador para mostrar sus estadisticas y descargarlo en csv\
    \n4) mostrar logros del jugador\
    \n5) calcular promedio de puntos por partidos del dream team\
    \n6) pregunatar si un jugador pertenece o no al salon de la fama del baloncesto\
    \n7)\
    \n8)\
    \n9)\
    \n10)\
    \n11)\
    \n12)\
    \n13)\
    \n14)\
    \n15)\
    \n16)\
    \n17)\
    \n18)\
    \n19)\
    \n20)")

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
                seleccionar_jugador_indice(jugadores)
            case 3:
                guardar_estadisticas_csv(jugadores)
            case 4:
                mostrar_logros_jugador(jugadores)
            case 5:
                calcular_promedio_puntos_por_partido_equipo(jugadores)
            case 6:
                mostrar_jugador_salon_fama(jugadores)
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
    

def seleccionar_jugador_indice(jugadores: list):
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

def guardar_estadisticas_csv(jugadores: list):
    """""
    recive como parametro una lista de jugadores 
    recorre la lista imprime los jugadores ordenados por indice y da a elejir uno
    y guarda en un archivo csv el resultado
    
    """""
    contenido = seleccionar_jugador_indice(jugadores)
    archivo = "estadisticas_jugador.csv"
    guardar_archivo_csv(archivo, contenido)

# 4) Permitir al usuario buscar un jugador por su nombre y mostrar sus logros, como campeonatos de la NBA,
# participaciones en el All-Star y pertenencia al Salón de la Fama del Baloncesto, etc.

def seleccionar_jugador_por_nombre()->str:
    """""
    da a elejir un nombre
    veriica que sea valido
    retorna el patron introducido
    
    """""
    nombre = input("Escribir nombre de jugador: ")
    patron = ""
    if re.match(r"^[A-Za-z ]{3}",nombre):
        patron = nombre
    else:
        imprimir_dato("Nombre inválido. Inténtelo nuevamente")
    return patron

def mostrar_logros_jugador(jugadores: list):
    """""
    recive una lista de jugadores
    da a elejir un nombre de jugador, verifica que sea valido
    imprime los logros del jugador
    
    """""
    patron = seleccionar_jugador_por_nombre()
    jugador_encontrado = None
    for jugador in jugadores:
        if re.search(patron, jugador['nombre']):
            jugador_encontrado = jugador
            break
    if jugador_encontrado is not None:
        imprimir_dato(f"Logros de: {jugador_encontrado['nombre']}")
        for logro in jugador_encontrado['logros']:
            print("- " + logro)
    else:
        print("Jugador no encontrado.")

# 5) Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team.

def calcular_promedio_puntos_por_partido_equipo(jugadores: list):
    """""
    recive una lista de jugadores
    recorre la lista y calcula el promedio de puntos por partido del equipo
    imprime el resultado
    
    """""
    acumulador_promedios = 0

    for jugador in jugadores:
      acumulador_promedios += jugador["estadisticas"]["promedio_puntos_por_partido"]
    
    promedio_puntos_por_partido = acumulador_promedios / len(jugadores)
    imprimir_dato(promedio_puntos_por_partido)

# 6) Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.

def mostrar_jugador_salon_fama(jugadores: list):
    """""
    recive una lista de jugadores
    da a eljir un nombre, verifica que sea valido
    imprime si pertenece o no al salon de la fama 

    """""
    patron = seleccionar_jugador_por_nombre()
    for jugador in jugadores:
        if re.search(patron, jugador['nombre']):
            jugador_encontrado = jugador
            break
    if jugador_encontrado is not None:
            if "Miembro del Salon de la Fama del Baloncesto" in jugador_encontrado["logros"]:
                imprimir_dato(f"{jugador_encontrado['nombre']} pertenece al salon de la fama del baloncesto")
            else:
                imprimir_dato(f"{jugador_encontrado['nombre']} no pertenece al salon de la fama del baloncesto")





        








    







    
    
    


    

