from datetime import datetime
import os

nombre = "Aline"
archivo_nombre = "asistencia.txt"

ahora = datetime.now()
fecha = ahora.strftime("%d/%m/%Y")
hora = ahora.strftime("%H:%M:%S")

# Crear archivo si no existe
if not os.path.exists(archivo_nombre):
    open(archivo_nombre, "w").close()

with open(archivo_nombre, "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

entrada_hoy = False
salida_hoy = False

for linea in lineas:
    if nombre in linea and fecha in linea:
        if "Entrada" in linea:
            entrada_hoy = True
        if "Salida" in linea:
            salida_hoy = True

# Lógica inteligente
if not entrada_hoy:
    tipo = "Entrada"
elif entrada_hoy and not salida_hoy:
    tipo = "Salida"
else:
    print("Ya registraste entrada y salida hoy 😏")
    exit()

registro = f"{nombre} | {tipo} | {fecha} | {hora}"

with open(archivo_nombre, "a", encoding="utf-8") as archivo:
    archivo.write(registro + "\n")

print(f"{tipo} registrada correctamente ✅")
