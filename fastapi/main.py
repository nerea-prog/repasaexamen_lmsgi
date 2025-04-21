from fastapi import FastAPI
from pydantic import BaseModel
import gestor

app = FastAPI()

class Alumne(BaseModel):
    id: int
    nom: str
    edat: int

@app.get("/")
def home():
    return{"Message" : "Benvingut a l'API d'alumnes"}

@app.get("/alumnes")
def tots():
    return gestor.cargar_alumnos

@app.get("/alumnes/{id}")
def veure(id: int):
    alumne = gestor.obtener_alumnos(id)
    if alumne:
        return alumne
    return {"error":"Alumne no trobat"}

@app.post("/alumnes")
def añadir(alumne: Alumne):
    if gestor.obtener_alumnos(alumne.id):
        return {"error":"ID ja existent"}
    gestor