import cv2
import os
from datetime import datetime

# Configuración de carpetas para evidencias
if not os.path.exists('Intrusos'):
    os.makedirs('Intrusos')

def procesar_seguridad(frame, nombre, rostro_ubicacion):
    top, right, bottom, left = rostro_ubicacion
    ahora = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    if nombre == "Desconocido":
        # Color ROJO para alertas
        color = (0, 0, 255)
        mensaje = "ALERTA: No registrado"
        
        # Guardar evidencia del intruso
        foto_path = f"Intrusos/desconocido_{ahora}.jpg"
        cv2.imwrite(foto_path, frame)
    else:
        # Color VERDE para usuarios registrados
        color = (0, 255, 0)
        mensaje = f"Bienvenido: {nombre}"

    # Dibujar el recuadro y el texto en pantalla
    cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
    cv2.putText(frame, mensaje, (left + 6, bottom - 6), 
                cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), 1)

    return frame