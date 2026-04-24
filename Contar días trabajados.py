archivo_nombre = "asistencia.txt"

dias = set()  # para no repetir fechas

with open(archivo_nombre, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        partes = linea.strip().split(" | ")
        
        nombre = partes[0]
        tipo = partes[1]
        fecha = partes[2]

        if tipo == "Entrada":
            dias.add(fecha)

print(f"Días trabajados: {len(dias)} 📅")
