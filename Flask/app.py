from flask import Flask, render_template

#Inicio de la aplicación(Todo va adentro)
app = Flask(__name__)

app.run(debug = True)

@app.route('/')
@app.route('/contacto')

def principal():
    return render_template('index.html')

def contacto():
    return "Contacto"

#Termina la aplicación
if __name__ == '__main__':
    app.run(debug = True, port = 3500)
