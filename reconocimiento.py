import cv2
import os
import numpy as np
import datetime
import pyttsx3

# 🔊 Inicializar voz
engine = pyttsx3.init()
engine.setProperty('rate', 150)

dataset_path = "dataset"

faces = []
labels = []
label_map = {}
current_label = 0

# Cargar imágenes
for nombre in os.listdir(dataset_path):
    ruta_persona = os.path.join(dataset_path, nombre)

    label_map[current_label] = nombre

    for archivo in os.listdir(ruta_persona):
        ruta_imagen = os.path.join(ruta_persona, archivo)
        imagen = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)

        if imagen is not None:
            faces.append(imagen)
            labels.append(current_label)

    current_label += 1

# Crear y entrenar modelo
modelo = cv2.face.LBPHFaceRecognizer_create()
modelo.train(faces, np.array(labels))

# Detector de rostro
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Cámara
cap = cv2.VideoCapture(0)

# 🔥 Evitar repetición de voz
ultimo_nombre = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostros = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in rostros:
        rostro = gray[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (200, 200))

        label, confianza = modelo.predict(rostro)

        # 👇 Mostrar en consola
        print("Confianza:", confianza)

        if confianza < 110:
            nombre = label_map.get(label, "Desconocido")

            if nombre == "Miku":
                texto = "Acceso permitido 💗"

                if ultimo_nombre != nombre:
                    engine.say("Acceso permitido")
                    engine.runAndWait()
                    ultimo_nombre = nombre
            else:
                texto = f"{nombre} detectado"

                if ultimo_nombre != nombre:
                    engine.say(f"{nombre} detectado")
                    engine.runAndWait()
                    ultimo_nombre = nombre

            # Guardar registro
            with open("registro_accesos.txt", "a") as f:
                ahora = datetime.datetime.now()
                f.write(f"{nombre} - {ahora}\n")

        else:
            texto = "Acceso denegado 🚫"
            ultimo_nombre = ""

        # Dibujar cuadro
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Mostrar texto + confianza
        cv2.putText(frame, f"{texto} ({int(confianza)})", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Reconocimiento Facial", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()