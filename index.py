from flask import Flask, render_template #add library

app = Flask(__name__)

"""
@app.route('/')
def principal():
    #return "Bienvenido a mi sitio web con Python"
    return "Buenas Buenas, o sii, como estamos?"

@app.route('/contacto')
def contacto():
    return "Esta es la pagina de contacto"
"""
@app.route('/')
def principal():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5010)