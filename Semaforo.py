import semaforo  # <--- Importas el archivo que acabas de crear

# ... (código donde detectas la cara) ...

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # 1. Buscas el nombre como ya lo hacías
    # nombre = buscar_nombre(face_encoding) 

    # 2. LLAMAS A TU NUEVO MÓDULO
    if nombre == "Desconocido":
        color = (255, 255, 255)
        status = "DENEGADO"
        # Aquí puedes poner el código de capturar la foto del intruso
    else:
        # Aquí usas la función de tu archivo semaforo.py
        color, status = semaforo.obtener_estatus_y_color()

    # 3. DIBUJAS LA INTERFAZ usando el módulo
    semaforo.dibujar_interfaz(frame, nombre, (top, right, bottom, left), color, status)