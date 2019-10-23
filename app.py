from flask import Flask, jsonify, request, render_template
import requests
app = Flask(__name__, template_folder="templates")

productos_list = ['Leche','Cacao', 'Carne', 'Flores','Hortalizas']

@app.route('/listCultivo', methods = ['GET'])
def listCultivo():
    cultivos_list = requests.get('/tipoCultivos').json()
    return render_template('listarCultivo.html', cultivos = cultivos_list)

@app.route('/ingreCultivo', methods = ['GET'])
def NewCultivo():
    return render_template('nuevoCultivo.html', variables = productos_list)

@app.route('/guardarCultivo', methods=['POST'])
def saveCultivo():
   cultivo = dict(request.values)
   cultivo['latitud'] = int(cultivo['latitud'])
   cultivo['longitud'] = int(cultivo['longitud'])
   cultivo['area'] = int(cultivo['area'])
   requests.post('/tipoCultivos', json=cultivo)
   return(listCultivo())