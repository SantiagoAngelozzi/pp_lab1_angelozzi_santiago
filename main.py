from biblioteca import leer_archivo_json, dream_team_app
ruta = r"C:\Users\angelozzi_22\Desktop\Nueva carpeta\pp_lab1_angelozzi_santiago\dt.json"
lista_jugadores = leer_archivo_json(ruta)
dream_team_app(lista_jugadores)