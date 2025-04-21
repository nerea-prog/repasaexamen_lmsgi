# Practica 1

'''noms = ["Nerea", "Alba", "Tefa"]
nom = "Alba"
def encuentra_nombre(noms, nom):
    for i in noms:
        if nom in noms:
            return True
        else:
            return False'''
'''result = encuentra_nombre(noms, nom)'''
'''if result == True:
    print("El nombre esta en la lista")
else:
    print("El nombre no esta en la lista")
'''

# Practica 2
'''noms = ["Nerea", "Alba", "Tefa"]
nom = "Tefa"
def posicion_nombre(llista, nom): 
    for i in range(len(llista)):
        if llista[i] == nom:
            return i
    return -1
resultado = posicion_nombre(noms, nom)
if resultado == -1:
    print("No se encuentra el resultado")
else:
    print("El nombre se encuentra en la posición ", resultado)
'''
# Practica 3 - IMPORTANTE MIRARMELO BASTANTE PORQUE PUEDE SALIR
miDiccionari = {}
def menu():
    while True:
        print("------- Menu --------")
        print("1. Mostrar diccionari")
        print("2. Afegir entrades")
        print("3. Mostrar entrada")
        print("4. Esborrar la entrada")
        print("5. Modificar la entrada")
        print("0. Sortir")

        entrada = input("Escull un numero ")

        if entrada == "1":
            for clau, valor in miDiccionari.items():
                print(f"{clau}: {valor}")
        elif entrada == "2":
            clau = input("Introdueix una clau: ")
            valor = input("Introdueix un valor: ")
            miDiccionari[clau] = valor
        elif entrada == "3":
            clau = input("Introdueix una clau: ")
            if clau in miDiccionari:
                print(f"Valor: {miDiccionari[clau]}")
            else:
                print("Clau no trobada")
        elif entrada == "4":
            clau = input("Introdueix una clau: ")
            if clau in miDiccionari:
                del miDiccionari[clau]
                print("Entrada esborrada")
            else:
                print("Clau no trobada")
        elif entrada == "5":
            clau = input("Introdueix un valor: ")
            if clau in miDiccionari:
                valor = input("Introdueix un valor: ")
                miDiccionari[clau] = valor
                print("Entrada modificada")
            else:
                print("Clau no trobada")
        elif entrada == "0":
            print("Sortint...")
            break
        else:
            print("Opció invalida")

menu()

# Practica FASTAPI - Version mejorada
from fastapi import FastAPI, Body
import json
import os

# Crear l’aplicació
app = FastAPI()

# Nom del fitxer on es guarden els alumnes
nom_fitxer = "alumnes.json"

# FUNCIONS DE SUPORT ##################################################

# Carregar alumnes del fitxer JSON
def carregar_alumnes():
    if os.path.exists(nom_fitxer):
        fitxer = open(nom_fitxer, "r", encoding="utf-8")
        dades = json.load(fitxer)
        fitxer.close()
        return dades
    else:
        return []

# Desar alumnes al fitxer JSON
def desar_alumnes(alumnes):
    fitxer = open(nom_fitxer, "w", encoding="utf-8")
    json.dump(alumnes, fitxer, indent=4)
    fitxer.close()

# RUTES DE L’API #######################################################

# Ruta principal
@app.get("/")
def home():
    return "Institut TIC de Barcelona"

# Ruta per saber quants alumnes hi ha
@app.get("/alumnes")
def total_alumnes():
    alumnes = carregar_alumnes()
    return {"total": len(alumnes)}

# Ruta per obtenir les dades d’un alumne pel seu ID
@app.get("/alumnes/{id_alumne}")
def obtenir_alumne(id_alumne: int):
    alumnes = carregar_alumnes()
    alumne_trobat = None

    for alumne in alumnes:
        if alumne["id"] == id_alumne:
            alumne_trobat = alumne
            break

    if alumne_trobat is None:
        return {"missatge": "Alumne no trobat"}

    return alumne_trobat

# Ruta per esborrar un alumne pel seu ID
@app.delete("/del/{id_alumne}")
def esborrar_alumne(id_alumne: int):
    alumnes = carregar_alumnes()
    nova_llista = []
    alumne_trobat = False
    for alumne in alumnes:
        if alumne["id"] != id_alumne:
            nova_llista.append(alumne)
        else:
            alumne_trobat = True

    if not alumne_trobat:
        return {"missatge": "Alumne no trobat"}

    desar_alumnes(nova_llista)
    return {"missatge": "Alumne esborrat"}

# Ruta per afegir un nou alumne
@app.post("/alumne/")
def afegir_alumne(alumne: dict = Body(..., example={
    "id": 1,
    "nom": "Nom de prova",
    "cognom": "Cognom de prova",
    "data": {
        "dia": "01",
        "mes": "gener",
        "any": "2000"
    },
    "email": "prova@exemple.com",
    "feina": "Estudiant",
    "curs": "DAW"
})):
    alumnes = carregar_alumnes()

    # Comprovar si l’ID ja existeix
    for a in alumnes:
        if a["id"] == alumne["id"]:
            return {"missatge": "ID ja existent"}

    alumnes.append(alumne)
    desar_alumnes(alumnes)
    return {"missatge": "Alumne afegit correctament"}

# GESTOR.PY
import os
import json

nom_fitxer = "alumnes.json"

def carregar_alumnes():
    if os.path.exists(nom_fitxer):
        with open(nom_fitxer, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def desar_alumnes(alumnes):
    with open(nom_fitxer, "w", encoding="utf-8") as f:
        json.dump(alumnes, f, indent=4)

def generar_id(alumnes):
    return max((a["id"] for a in alumnes), default=0) + 1

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Gestió alumnes\n" + "-"*30)
    print("1. Mostrar alumnes")
    print("2. Afegir alumne")
    print("3. Veure alumne")
    print("4. Esborrar alumne")
    print("0. Sortir\n")
    return input("Opció > ")

### ─── Bucle Principal ───────────────────────────────────────────
while True:
    opcio = menu()
    alumnes = carregar_alumnes()

    ### ─── Mostrar alumnes ─────────────────────
    if opcio == "1":
        print("\nLlista d’alumnes\n" + "-"*30)
        
        # Bucle per mostrar cada alumne:
        for a in alumnes:
            print(f"{a['id']}: {a['nom']} {a['cognom']}")
        
        input("\nPrem una tecla per continuar...")

    ### ─── Afegir alumne ─────────────────────
    elif opcio == "2":
        print("\nAfegir alumne\n" + "-"*30)
        
        nou = {
            "id": generar_id(alumnes),
            "nom": input("Nom: "),
            "cognom": input("Cognom: "),
            "edat": input("Edat: "),
            "email": input("Email: "),
            "feina": input("Té feina? (s/n): ").lower() == "s",
            "curs": input("Curs: ")
        }

        alumnes.append(nou)  # Afegim el nou alumne a la llista

        desar_alumnes(alumnes)
        print("✅ Alumne afegit!")
        input()

    ### ─── Veure alumne ─────────────────────
    elif opcio == "3":
        print("\nVeure alumne\n" + "-"*30)
        id_buscat = int(input("ID: "))

        # Bucle per buscar l'alumne amb l'ID:
        alumne = None
        for a in alumnes:
            if a["id"] == id_buscat:
                alumne = a
                break

        if alumne:
            print(json.dumps(alumne, indent=4))
        else:
            print("❌ Alumne no trobat")

        input()

    ### ─── Esborrar alumne ─────────────────────
    elif opcio == "4":
        print("\nEsborrar alumne\n" + "-"*30)
        id_esborrar = int(input("ID: "))

        # Bucle per eliminar l'alumne:
        alumnes_nous = []
        for a in alumnes:
            if a["id"] != id_esborrar:
                alumnes_nous.append(a)

        desar_alumnes(alumnes_nous)
        print("🗑️ Alumne esborrat correctament!")
        input()

    ### ─── Sortir del programa ─────────────────────
    elif opcio == "0":
        print("👋 Fins aviat!")
        break

    ### ─── Opció no vàlida ─────────────────────
    else:
        print("❗ Opció no vàlida")
        input()


