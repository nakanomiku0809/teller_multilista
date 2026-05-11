from flask import Flask, render_template, jsonify
from logica import cargar_todo, pasar_a_diccionario

app = Flask(__name__)
toda_la_lista = cargar_todo()

@app.route('/')
def pagina_principal():
    return render_template('mapa.html')

@app.route('/datos')
def enviar_json():
    diccionario = pasar_a_diccionario(toda_la_lista)
    return jsonify(diccionario)

if __name__ == '__main__':
    app.run(debug=True, port=8080)