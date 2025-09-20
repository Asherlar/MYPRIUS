# BACKEND/FastAPI/main.py 
# Importamos FastAPI y CORSMiddleware para manejar CORS (Cross-Origin Resource Sharing)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir peticiones desde frontend local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringir esto a tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint que recibe/captura los KMs y devuelve un json con el color y mensaje correspondiente al frontend
@app.get("/2/{kms}")
def get_kms(kms: int):
    color = "white"
    msg = ""
    if kms > 20000:
        color = "red"
        msg = "Cambio necesario"
    else:
        color = "green"
        msg = "Cambio no necesario"
    return {"color": color, "msg": msg}