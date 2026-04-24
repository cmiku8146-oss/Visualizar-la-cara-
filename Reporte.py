nombre = "Aline"

# Cambia esto a True o False
puntual = False   # True = puntual / False = con retardos

if puntual:
    reporte = f"""
REPORTE DE PUNTUALIDAD

Nombre: {nombre}

----------------------------------------

Descripción:
Se hace constar que {nombre} ha demostrado
responsabilidad y compromiso en su puntualidad.

Puntualidad:
- Llega a tiempo constantemente
- Cumple con horarios establecidos
- Mantiene disciplina

Conclusión:
Excelente nivel de puntualidad.

----------------------------------------
Firma: ____________________
Fecha: ____________________
"""
else:
    reporte = f"""
REPORTE DE PUNTUALIDAD

Nombre: {nombre}

----------------------------------------

Descripción:
Se ha observado que {nombre} presenta
algunas inconsistencias en su puntualidad.

Observaciones:
- Presenta llegadas tardías ocasionales
- Requiere mejorar el cumplimiento de horarios
- Se recomienda mayor organización

Conclusión:
Se sugiere mejorar la puntualidad para
cumplir adecuadamente con sus responsabilidades.

----------------------------------------
Firma: ____________________
Fecha: ____________________
"""

# Guardar archivo
with open("reporte_puntualidad.txt", "w", encoding="utf-8") as archivo:
    archivo.write(reporte)

print("Reporte generado 💗")