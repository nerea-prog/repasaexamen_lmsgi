import os
import json

fitxer = "alumnes.json"

def carregar():
    if os.path.exists(fitxer):
        f = open(fitxer, "r", encoding= "utf-8")
        dades = json.load(f)
        f.close()
        return dades
    return []

def desar(alumnes):
    f = open(fitxer, "r", encoding="utf-8")
    json.dump(alumnes, f, indent=4)
    f.close()

def afegir():
    