"""""""""
Santiago Angelozzi
DIV-E
Parcial
"""""""""
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
    imprimir_dato("1) Mostrar la lista de todos los jugadores del Dream Team.\
    \n2) elije un jugador para mostrar sus estadisticas.\
    \n3) elije un jugador para mostrar sus estadisticas y descargarlo en csv.\
    \n4) mostrar logros del jugador.\
    \n5) calcular promedio de puntos por partidos del dream team.\
    \n6) pregunatar si un jugador pertenece o no al salon de la fama del baloncesto.\
    \n7) Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.\
    \n8) Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.\
    \n9) Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.\
    \n10) ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.\
    \n11) ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.\
    \n12) ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.\
    \n13) Calcular y mostrar el jugador con la mayor cantidad de robos totales.\
    \n14) Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.\
    \n15) ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.\
    \n16) Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.\
    \n17) Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos\
    \n18) ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.\
    \n19) Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas\
    \n20) ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.")

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
                lista_ordenada = quick_sort_estadisticas(jugadores, "rebotes_totales", False)
                imprimir_dato(f"el jugador con mayor cantidad de rebotes totales es: {lista_ordenada[0]['nombre']} y la cantidad es: {lista_ordenada[0]['estadisticas']['rebotes_totales']}")
            case 8:
                lista_ordenada = quick_sort_estadisticas(jugadores, "porcentaje_tiros_de_campo", False)
                imprimir_dato(f"el jugador con mayor porcentaje de tiros de campo es: {lista_ordenada[0]['nombre']} y el porcemtaje es: {lista_ordenada[0]['estadisticas']['porcentaje_tiros_de_campo']}")
            case 9:
                lista_ordenada = quick_sort_estadisticas(jugadores, "promedio_asistencias_por_partido", False)
                imprimir_dato(f"el jugador con mayor promedio de asistencia por partido es: {lista_ordenada[0]['nombre']} y el promedio es: {lista_ordenada[0]['estadisticas']['promedio_asistencias_por_partido']}")
            case 10:
                mostrar_jugador_mayor_al_valor(jugadores, "promedio_puntos_por_partido")               
            case 11:
                mostrar_jugador_mayor_al_valor(jugadores, "promedio_rebotes_por_partido")
            case 12:
                mostrar_jugador_mayor_al_valor(jugadores, "promedio_asistencias_por_partido")
            case 13:
                lista_ordenada = quick_sort_estadisticas(jugadores, "robos_totales", False)
                imprimir_dato(f"el jugador con mayor cantidad de robos totales es: {lista_ordenada[0]['nombre']} y la cantidad es: {lista_ordenada[0]['estadisticas']['robos_totales']}")
            case 14:
                lista_ordenada = quick_sort_estadisticas(jugadores, "bloqueos_totales", False)
                imprimir_dato(f"el jugador con mayor cantidad de bloqueos totales es: {lista_ordenada[0]['nombre']} y la cantidad es: {lista_ordenada[0]['estadisticas']['bloqueos_totales']}")
            case 15:
                mostrar_jugador_mayor_al_valor(jugadores, "porcentaje_tiros_libres")
            case 16:
                imprimir_dato(f"el promedio de puntos por partido del equipo sacando al que menos promedio hizo es: ")
                promedios_menos_el_peor(jugadores, "promedio_puntos_por_partido", True)
            case 17:
                jugador_con_mas_logros(jugadores)
            case 18:
                mostrar_jugador_mayor_al_valor(jugadores, "porcentaje_tiros_triples")
            case 19:
                lista_ordenada = quick_sort_estadisticas(jugadores, "temporadas", False)
                imprimir_dato(f"el jugador con mayor cantidad de temporadas es: {lista_ordenada[0]['nombre']} y la cantidad es: {lista_ordenada[0]['estadisticas']['temporadas']}")
            case 20:
                pass
        clear_console()

#1)
def mostrar_jugadores(jugadores: list):
    """""
    recive como parametro una lista de jugadores
    recorre la lista  imprime nombre y pocicion de los jugadores
    
    """""
    if jugadores:
        for jugador in jugadores:
            imprimir_dato(f"{jugador['nombre']} - {jugador['posicion']}")
#2) 
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
        return dato
    else:
        print("Índice de jugador inválido.")    
# 3)
def guardar_estadisticas_csv(jugadores: list):
    """""
    recive como parametro una lista de jugadores 
    recorre la lista imprime los jugadores ordenados por indice y da a elejir uno
    y guarda en un archivo csv el resultado
    
    """""
    contenido = seleccionar_jugador_indice(jugadores)
    if contenido == None:
        return "no se pudo realizar la operacion"
    else:
        archivo = "estadisticas_jugador.csv"
        guardar_archivo_csv(archivo, contenido)
# 4)
def seleccionar_jugador_por_nombre() -> str:
    """""
    da a elejir un nombre
    veriica que sea valido
    retorna el patron introducido
    
    """""
    nombre = input("Escribir nombre de jugador: ")
    patron = ""
    if re.match(r"^[A-Za-z ]{3}",nombre):
        patron = nombre
        return patron
    else:
       imprimir_dato("Nombre inválido. Inténtelo nuevamente")
       return -1

def mostrar_logros_jugador(jugadores: list):
    """""
    recive una lista de jugadores
    da a elejir un nombre de jugador, verifica que sea valido
    imprime los logros del jugador
    
    """""
    jugador_encontrado = None
    patron = seleccionar_jugador_por_nombre()
    if patron == -1:
        pass
    else:
        for jugador in jugadores:
            if re.search(patron, jugador['nombre']):
                jugador_encontrado = jugador
                break
        if jugador_encontrado is not None:
            imprimir_dato(f"Logros de: {jugador_encontrado['nombre']}")
            for logro in jugador_encontrado['logros']:
                print("- " + logro)
        else: 
            print("Nombre inválido. Inténtelo nuevamente")
#5)
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
#6)
def mostrar_jugador_salon_fama(jugadores: list):
    """""
    recive una lista de jugadores
    da a eljir un nombre, verifica que sea valido
    imprime si pertenece o no al salon de la fama 

    """""
    patron = seleccionar_jugador_por_nombre()
    jugador_encontrado = None
    if patron == -1:
        pass
    else:
        for jugador in jugadores:
            if re.search(patron, jugador['nombre']):
                jugador_encontrado = jugador
                break
        if jugador_encontrado is not None:
                if "Miembro del Salon de la Fama del Baloncesto" in jugador_encontrado["logros"]:
                    imprimir_dato(f"{jugador_encontrado['nombre']} pertenece al salon de la fama del baloncesto")
                elif "Miembro del Salon de la Fama del Baloncesto" not in jugador_encontrado["logros"]:
                    imprimir_dato(f"{jugador_encontrado['nombre']} no pertenece al salon de la fama del baloncesto")
        else:
            ("Nombre inválido. Inténtelo nuevamente")
#7)-8)-9)-13)-14)-19)
def quick_sort_estadisticas(jugadores:list,dato:str,flag:bool):
    """""
    recive una lista de jugadores y un dato tipo str y un flag tipo bool
    los ordena de manera decendente o acendente depende el flag y segun el dato
    devuele la lista ordenada

    """""
    lista_de = []
    lista_iz = []
    if len(jugadores) <= 1:
            return jugadores
    else:
        cantidad = len(jugadores)
        pivot = jugadores[0]
        for i in range(1,cantidad):
            if flag == True and jugadores[i]["estadisticas"][dato] > pivot["estadisticas"][dato] or flag == False and jugadores[i]["estadisticas"][dato] < pivot["estadisticas"][dato]:
                lista_de.append(jugadores[i])
            elif flag == True and jugadores[i]["estadisticas"][dato] <= pivot["estadisticas"][dato] or flag == False and jugadores[i]["estadisticas"][dato] > pivot["estadisticas"][dato]:
                lista_iz.append(jugadores[i])
    lista_iz = quick_sort_estadisticas(lista_iz,dato,flag)
    lista_iz.append(pivot)
    lista_de = quick_sort_estadisticas(lista_de,dato,flag)
    lista_iz.extend(lista_de)
    return lista_iz
# 10)-11)-12)-15)-18)
def mostrar_jugador_mayor_al_valor(jugadores:list, dato: str):
    """""
    recive una lista de jugadores y un dato tipo str
    pide ingresar un valor y crea una nueva lista con los mayores a ese valor
    si la lista contiene algo imprime los elementos y si no contiene nada lo notifica

    """""
    valor = float(input("ingrese un valor: "))
    lista_aux = []
    for jugador in jugadores:
        dato_actual = jugador["estadisticas"][dato]
        if dato_actual > valor:
            lista_aux.append(jugador["nombre"])
    
    if lista_aux:
        imprimir_dato(f"los jugadores que superan el valor de {valor} son: {lista_aux}")
    else:
        imprimir_dato(f"ningun jugador supero el valor de {valor}")
#16)
def promedios_menos_el_peor(jugadores: list, dato: str, flag: bool):
    """""
    recive una lista de jugadores, un dato tipo str y una flag tipo bool
    ordena la lista segun el dato y el flag y saca el primer elemento de la lista luego calcula el promedio de la nueva lista ordenada
    retorna el promedio

    """""
    lista_ordenada = quick_sort_estadisticas(jugadores, dato, flag)
    lista_ordenada.pop(0)
    nuevo_promedio = calcular_promedio_puntos_por_partido_equipo(lista_ordenada)
    return nuevo_promedio    
#17)
def jugador_con_mas_logros(jugadores):
    """""
    recive una lista de jugadores 
    recorre la lista y guarda en una lista auxiliar los len de logros de cada jugador decubriendo quiem es jugador con el maximo de logros
    imprime el nombre del jugador y el len de sus logros.
    """""
    cantidades_logros = []
    for jugador in jugadores:
        cantidad_logros = len(jugador["logros"])
        cantidades_logros.append(cantidad_logros)
        mayor_cantidad_logros = max(cantidades_logros)
        if len(jugador["logros"]) == mayor_cantidad_logros:
            print(f"El jugador con mas logros es {jugador['nombre']} y la cantidad de logros es {mayor_cantidad_logros}")



