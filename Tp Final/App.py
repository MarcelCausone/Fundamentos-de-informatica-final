from flask import Flask, render_template, request, redirect, flash
import csv
from Functions import cargar_datos, promedio_por_materia,nota_mayor_a,notas_bajas,contar_aprobados_por_materia
from ordenamientos import  ordenar_por_promedio_burbuja, ordenar_por_promedio_seleccion
app = Flask(__name__)
app.secret_key = 'clave-super-secreta-123'  # <--- acá debe ir, justo después de crear la app

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form['nombre']
    materia = request.form['materia']
    
    try: 
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
    except ValueError:
        flash('Por favor, ingrese valores numéricos válidos para las notas.')
        return redirect('/formulario')
    
    if not (1<= nota1 <= 10 and 1 <= nota2 <= 10 and 1 <= nota3 <= 10):
        flash('Las notas deben estar entre 1 y 10.')
        return redirect('/formulario')
        
    nota_final = round((nota1 + nota2 + nota3) / 3, 2)

    with open('notas.csv', mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre, materia, nota1, nota2, nota3, nota_final])
        
    flash(f'Notas guardadas correctamente para {nombre} en {materia}. Nota final: {nota_final}')
    return redirect('/')

@app.route('/notas')
def notas():
    orden = request.args.get('orden', default='ninguno')
    alumnos = cargar_datos()

    if orden == 'burbuja':
        alumnos = ordenar_por_promedio_burbuja(alumnos)
    elif orden == 'seleccion':
        alumnos = ordenar_por_promedio_seleccion(alumnos)

    return render_template("listadoGeneral.html", alumnos=alumnos, orden=orden)

@app.route("/informe1")
def informe1():
    datos = cargar_datos()
    resultado = promedio_por_materia(datos)
    return render_template("informe1.html", resultado=resultado)
    
@app.route("/informe2")
def informe2():
    datos = cargar_datos()
    umbral = request.args.get('umbral', default=6.0, type=float)
    resultado = nota_mayor_a(datos, umbral)
    return render_template("informe2.html", resultado=resultado, umbral=umbral)

@app.route("/informe3")
def informe3():
    datos = cargar_datos()
    resultado = notas_bajas(datos)
    return render_template("informe3.html", resultado= resultado)

@app.route("/informe4")
def informe4():
    datos = cargar_datos()
    resultado = contar_aprobados_por_materia(datos)
    return render_template("informe4.html", resultado=resultado)





if __name__ == '__main__':
    app.run(debug=True)
