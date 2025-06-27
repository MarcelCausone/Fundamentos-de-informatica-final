from flask import Flask, render_template, request, redirect, flash
import csv
import os
from Functions import cargar_datos, promedio_por_materia,nota_mayor_a,notas_bajas,contar_aprobados_por_materia
from ordenamientos import  ordenar_por_promedio_burbuja, ordenar_por_promedio_seleccion
from werkzeug.utils import secure_filename
#Inicializacion de la aplicacion Flask
app = Flask(__name__)
app.secret_key = 'clave-super-secreta-123'  # <--- acá debe ir, justo después de crear la app      Necesario para usar flash messages
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
#Muestra la pagina de inicio y sus botones
@app.route('/')
def inicio():
    return render_template('index.html')
#Muestra el formulario para ingresar alumnos
@app.route('/formulario')
def formulario():
    return render_template('formulario.html')
#Envio de fomulario
@app.route('/enviar', methods=['POST'])
def enviar(): #obtiene los datos del formulario
    nombre = request.form['nombre']
    materia = request.form['materia']
    
    try:  #convierte notas a float y valida que sean numeros
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
    except ValueError:
        flash('Por favor, ingrese valores numéricos válidos para las notas.')
        return redirect('/formulario')
    #Valida que las notas esten entre 1 y 10
    if not (1<= nota1 <= 10 and 1 <= nota2 <= 10 and 1 <= nota3 <= 10):
        flash('Las notas deben estar entre 1 y 10.')
        return redirect('/formulario')
    #calcula promedio redondeando a 2 decimales
    nota_final = round((nota1 + nota2 + nota3) / 3, 2)
    #guarda datos en el csv
    with open('notas.csv', mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre, materia, nota1, nota2, nota3, nota_final])
     #imprime mensaje de exito y dirige a inicio   
    flash(f'Notas guardadas correctamente para {nombre} en {materia}. Nota final: {nota_final}')
    return redirect('/')
#muestra el listado de alumnos con opcion de ordenar
@app.route('/notas')
def notas():
    orden = request.args.get('orden', default='ninguno') #obtiene el parametro de orden
    alumnos = cargar_datos()
    #aplica el ordenamiento segun lo recibido
    if orden == 'burbuja':
        alumnos = ordenar_por_promedio_burbuja(alumnos)
    elif orden == 'seleccion':
        alumnos = ordenar_por_promedio_seleccion(alumnos)

    return render_template("listadoGeneral.html", alumnos=alumnos, orden=orden)
#muestra el informe de promedios por materia
@app.route("/informe1")
def informe1():
    datos = cargar_datos()
    resultado = promedio_por_materia(datos)
    return render_template("informe1.html", resultado=resultado)
  #muestra almunos con notas mayores a un umbral  (6.0 predeterminado)
@app.route("/informe2")
def informe2():
    datos = cargar_datos()
    umbral = request.args.get('umbral', default=6.0, type=float)
    resultado = nota_mayor_a(datos, umbral)
    return render_template("informe2.html", resultado=resultado, umbral=umbral)
#muestra alumnos con notas menores a 4
@app.route("/informe3")
def informe3():
    datos = cargar_datos()
    resultado = notas_bajas(datos)
    return render_template("informe3.html", resultado= resultado)
#muestra conteo de aprobados/desaprobados 
@app.route("/informe4")
def informe4():
    datos = cargar_datos()
    resultado = contar_aprobados_por_materia(datos)
    return render_template("informe4.html", resultado=resultado)

import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/cargar_csv', methods=['GET', 'POST'])
def cargar_csv():
    if request.method == 'POST':
        if 'archivo' not in request.files:
            flash('No se encontró el archivo.')
            return redirect(request.url)

        archivo = request.files['archivo']

        if archivo.filename == '':
            flash('No se seleccionó ningún archivo.')
            return redirect(request.url)

        if archivo and allowed_file(archivo.filename):
            filename = secure_filename("temporal.csv")
            ruta_temporal = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            archivo.save(ruta_temporal)

            # Leer datos de notas.csv existentes
            datos_existentes = []
            if os.path.exists('notas.csv'):
                with open('notas.csv', newline='', encoding='utf-8') as f:
                    datos_existentes = list(csv.reader(f))

            # Leer nuevos datos desde temporal.csv
            nuevos_datos = []
            with open(ruta_temporal, newline='', encoding='utf-8') as f:
                lector = csv.reader(f)
                for fila in lector:
                    if len(fila) >= 6:
                        nuevos_datos.append(fila)

            # Unir y guardar de nuevo todo en notas.csv
            with open('notas.csv', mode='w', newline='', encoding='utf-8') as f:
                escritor = csv.writer(f)
                for fila in datos_existentes:
                    escritor.writerow(fila)
                for fila in nuevos_datos:
                    escritor.writerow(fila)

            flash(f'Se cargaron {len(nuevos_datos)} registros desde el CSV subido.')
            return redirect('/')
        else:
            flash('Tipo de archivo no permitido. Solo se permiten archivos .csv')
            return redirect(request.url)

    return render_template('cargar_csv.html')


if __name__ == '__main__':
    app.run(debug=True)
