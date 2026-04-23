from flask import Flask, render_template

# Inicio de la aplicación (todo va adentro)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/lenguajes')
def lenguajes():
    return render_template('lenguajes.html')

# Termina la aplicación
if __name__ == '__main__':
    app.run(debug=True, port=3500)