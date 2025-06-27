# 📚 Sistema de Gestión de Alumnos

## 📘 Descripción

Este proyecto en Python implementa un sistema para gestionar las calificaciones de alumnos a partir de un archivo CSV. Permite consultar, procesar, agregar y ordenar los datos de manera eficiente.

Cada línea del archivo CSV tiene el siguiente formato:

> ⚠️ **NotaFinal** es calculada automáticamente como el promedio de las tres notas.

---

## ✅ Requisitos del Sistema

1. **Carga de datos desde archivo CSV**  
   - Los datos se guardan en una **lista de listas** (matriz).

2. **Carga manual de alumnos**
   - Permite ingresar datos por teclado.
   - Calcula automáticamente el promedio final del alumno.

3. **Generación de Informes (mínimo 5)**:
   - Listado completo de alumnos con sus notas y promedio.
   - Promedio general por materia.
   - Alumnos con nota final mayor a un valor dado.
   - Alumnos con al menos una nota menor a 4.
   - Cantidad de aprobados y desaprobados por materia.

4. **Ordenamiento de datos**
   - Por **nombre del alumno**.
   - Por **nota final** (de mayor a menor).
   - Deben implementarse **al menos dos métodos de ordenamiento** (ej. burbuja y selección).

---

## 🧩 Organización del Código

- Uso de **funciones** para separar claramente cada operación:
  - Carga desde CSV
  - Carga manual
  - Generación de informes
  - Métodos de ordenamiento

- **Validación de datos**:
  - Las notas deben estar entre **0 y 10**.

- **Comentarios** en el código que expliquen claramente cada bloque funcional.

---

## ⚙️ Tecnologías

- Python 3.7+
- Flask (para frontend web, si aplica)
- HTML/CSS con Bootstrap (para la interfaz web, si aplica)


