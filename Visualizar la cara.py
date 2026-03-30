import cv2
import os

# Archivo de nombres
archivo_nombres = "personas.txt"

# Pedir nombre
nombre = input("Ingresa el nombre: ").strip().capitalize()

# Guardar nombre
if not os.path.exists(archivo_nombres):
    with open(archivo_nombres, "w") as f:
        f.write(nombre + "\n")
else:
    with open(archivo_nombres, "r") as f:
        nombres = f.read().splitlines()

    if nombre not in nombres:
        with open(archivo_nombres, "a") as f:
            f.write(nombre + "\n")

# Crear carpeta
dataset_path = "dataset"
ruta_persona = os.path.join(dataset_path, nombre)
os.makedirs(ruta_persona, exist_ok=True)

# Cámara
cap = cv2.VideoCapture(0)
contador = 0

print("Presiona 'S' para guardar fotos y 'ESC' para salir")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Registro de rostro", frame)

    tecla = cv2.waitKey(1)

    # Guardar imagen
    if tecla == ord('s'):
        nombre_archivo = os.path.join(ruta_persona, f"foto_{contador}.jpg")
        cv2.imwrite(nombre_archivo, frame)
        print(f"Imagen guardada: {nombre_archivo}")
        contador += 1

    # Salir
    if tecla == 27:
        break

cap.release()
cv2.destroyAllWindows()