from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':

        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3

        estado = 'Aprobado' if (promedio >= 40 and asistencia >= 75) else 'Reprobado'

        return render_template('Ejercicio1.html', promedio=promedio, estado=estado)

    return render_template('Ejercicio1.html')

@app.route('/Ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']


        nombres = [nombre1, nombre2, nombre3]
        nombre_largo = max(nombres, key=len)
        cantidad_caracteres = len(nombre_largo)

        return render_template('Ejercicio2.html', nombre_largo= nombre_largo, cantidad_caracteres= cantidad_caracteres)

    return render_template('Ejercicio2.html')

if __name__ == '__main__':
    app.run()
