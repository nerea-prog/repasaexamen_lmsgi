# Practica 1 modulos
import repasaexamen_lmsgi.practicar as practicar

noms = noms = ["Nerea", "Alba", "Tefa"]
nom = "Nerea"
result = practicar.encuentra_nombre(noms, nom)

if result == True:
    print("El nombre esta en la lista")
else:
    print("El nombre no esta en la lista")   

# Practica 2 modulos
'''import practicar

noms = ["Nerea", "Alba", "Tefa"]
nom = "Nerea"

posicion = practicar.posicion_nombre(noms, nom)

if posicion == -1:
    print("No se encuentra en ninguna posicion")
else:
    print(nom, "se encuentra en la posicion", posicion)'''