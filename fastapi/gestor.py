import json
import os

fitxer = "alumnes.json"

def cargar_alumnos():
    if os.path.exists(fitxer):
        f = open(fitxer, "r", encoding="utf-8")
        datos = json.load(f)
        f.close()
        return datos
    return[]

def guardar_alumnes(alumnes):
    f = open(fitxer, "r", encoding="utf-8")
    json.dump(alumnes, f, indent=4)
    f.close()

def añadir_alumnos(nuevo):
    alumnes = cargar_alumnos()
    alumnes.append(nuevo)
    guardar_alumnes(alumnes)
    return True

def obtener_alumnos(id):
    alumnes = cargar_alumnos()
    for i in alumnes:
        if i["id"] == id:
            return i
    return None

def eliminar_alumno(id):
    alumnes = cargar_alumnos()
    nous = []
    for i in alumnes:
        if i["id"] != id:
            nous.append[i]
    guardar_alumnes(nous)
    return True
