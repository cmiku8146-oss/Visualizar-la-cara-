from datetime import datetime

nombre = "Aline"
desempeno_bueno = True

fecha_actual = datetime.now().strftime("%d/%m/%Y")

if desempeno_bueno:
    reporte = f"""
REPORTE DE DESEMPEÑO

Nombre: {nombre}

----------------------------------------

Descripción:
Se hace constar que {nombre} ha mostrado un excelente desempeño.

Puntos positivos:
- Responsabilidad
- Buen trabajo en equipo
- Cumplimiento de tareas

Conclusión:
Desempeño sobresaliente.

----------------------------------------
Firma: ____________
Fecha: {fecha_actual}
"""
else:
    reporte = f"""
REPORTE DE DESEMPEÑO

Nombre: {nombre}

----------------------------------------

Descripción:
Se ha observado que {nombre} necesita mejorar su desempeño.

Observaciones:
- Falta de organización
- Entregas tardías
- Baja participación

Conclusión:
Se recomienda mejorar el rendimiento.

----------------------------------------
Firma: ____________
Fecha: {fecha_actual}
"""

# Nombre del archivo dinámico
nombre_archivo = f"reporte_{nombre}.txt"

with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    archivo.write(reporte)

print(f"Reporte guardado como {nombre_archivo} 💾")