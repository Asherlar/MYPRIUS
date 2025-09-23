# BACKEND/FastAPI/main.py 
# Importamos FastAPI y CORSMiddleware para manejar CORS (Cross-Origin Resource Sharing)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Importamos mysql.connector para conectar con la base de datos MySQL
import mysql.connector
import os

# Configuración de la conexión a la base de datos MySQL
# Asegúrate de configurar estas variables de entorno o reemplazarlas con tus credenciales
# Por ejemplo: USERNAME='root', PASSWORD='your_password', HOST='localhost', DATABASE='mydatabase'
db_config = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASSWORD", "David2025"),
    "database": os.environ.get("DB_NAME", "base_prius"),
}
# Función para conectar a la base de datos CONECTOR MYSQL
def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None

# Crear la instancia de FastAPI (inicia FastAPI)
app = FastAPI()

# Permitir peticiones desde frontend local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials="",
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint que recibe/captura los KMs y devuelve un json con el color y mensaje correspondiente al frontend
@app.get("/2/{kms}")
def get_kms(kms: int):
    print(f"Received kms: {kms}") # Línea para depuración
    conn = get_db_connection()
    if not conn:
        print("Database connection failed")  # Línea para depuración
        return {"error": "No se pudo conectar a la base de datos"}
# Realizamos la consulta a la base de datos, mediante el cursor
    cursor = conn.cursor()
    cursor.execute("SELECT odo_coche,kms_base_cmb_rdel,kms_act_rdel FROM general")
    result = cursor.fetchone()
    
# Inicializamos las variables de color y mensaje
    color = "white"
    msg = ""

# Si se obtienen resultados de la consulta, calculamos los valores necesarios y determinamos el color y mensaje
    if result:
        odo_coche, kms_base_cmb_rdel, kms_act_rdel = result
        print(f"odo_coche: {odo_coche}, kms_base_cmb_rdel: {kms_base_cmb_rdel}, kms_act_rdel: {kms_act_rdel}")
        
        difkmsrdel = kms - odo_coche
        vidaactrdel = kms_act_rdel + difkmsrdel
        complimrdel = kms_base_cmb_rdel - vidaactrdel
        print(f"difkmsrdel: {difkmsrdel}, vidaactrdel: {vidaactrdel}, complimrdel: {complimrdel}")


        if complimrdel <= 0:
            color = "red"
            msg = "Cambio necesario"
        else:
            color = "green"
            msg = "Cambio no necesario" + f" (Quedan {complimrdel} kms)"
    else:
        return {"error": "No se encontraron datos en la base de datos"}
    cursor.close()
    conn.close()

    return {"color": color, "msg": msg}