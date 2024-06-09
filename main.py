from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorCategoria import ControladorCategoria
from Controladores.ControladorIngreso import ControladorIngreso
from Controladores.ControladorEgreso import ControladorEgreso

app=Flask(__name__)
"""
los cors permiten hacer pruebas al servidor desde la misma maquina en la que esta corriendo el proyecto 
"""
cors = CORS(app)



"""
Implementacion de los controladores--------------------------------
"""


miControladorCategoria=ControladorCategoria()
miControladorIngreso=ControladorIngreso()
miControladorEgreso=ControladorEgreso()


"""
----------------------------------------------SERVICIOS CATEGORIAS___________________________________________________________________________
"""

@app.route("/categorias",methods=['GET'])
def getCategorias():
    json=miControladorCategoria.index()
    return jsonify(json)

@app.route("/categorias",methods=['POST'])
def crearCategoria():
    data = request.get_json()
    json=miControladorCategoria.create(data)
    return jsonify(json)

@app.route("/categorias/<string:id>",methods=['GET'])
def getCategoria(id):
    json=miControladorCategoria.show(id)
    return jsonify(json)

@app.route("/categorias/<string:id>",methods=['PUT'])
def modificarCategoria(id):
    data = request.get_json()
    json=miControladorCategoria.update(id,data)
    return jsonify(json)

@app.route("/categorias/<string:id>",methods=['DELETE'])
def eliminarCategoria(id):
    json=miControladorCategoria.delete(id)
    return jsonify(json)


"""
----------------------------------------------SERVICIOS INGRESOS___________________________________________________________________________
"""

@app.route("/ingresos",methods=['GET'])
def getIngresos():
    json=miControladorIngreso.index()
    return jsonify(json)

@app.route("/ingresos",methods=['POST'])
def crearIngreso():
    data = request.get_json()
    json=miControladorIngreso.create(data)
    return jsonify(json)

@app.route("/ingresos/<string:id>",methods=['GET'])
def getIngreso(id):
    json=miControladorIngreso.show(id)
    return jsonify(json)

@app.route("/ingresos/<string:id>",methods=['PUT'])
def modificarIngreso(id):
    data = request.get_json()
    json=miControladorIngreso.update(id,data)
    return jsonify(json)

@app.route("/ingresos/<string:id>",methods=['DELETE'])
def eliminarIngreso(id):
    json=miControladorIngreso.delete(id)
    return jsonify(json)

"""
metodo de relacion categoria  - ingresos
"""

@app.route("/ingresos/<string:id>/categoria/<string:id_categoria>", methods=['PUT'])
def asignarCategoriaAIngreso(id, id_categoria):
    json = miControladorIngreso.asignarCategoria(id, id_categoria)
    return jsonify(json)


"""
----------------------------------------------SERVICIOS EGRESOS___________________________________________________________________________
"""

@app.route("/egresos",methods=['GET'])
def getEgresos():
    json=miControladorEgreso.index()
    return jsonify(json)

@app.route("/egresos",methods=['POST'])
def crearEgreso():
    data = request.get_json()
    json=miControladorEgreso.create(data)
    return jsonify(json)

@app.route("/egresos/<string:id>",methods=['GET'])
def getEgreso(id):
    json=miControladorEgreso.show(id)
    return jsonify(json)

@app.route("/egresos/<string:id>",methods=['PUT'])
def modificarEgreso(id):
    data = request.get_json()
    json=miControladorEgreso.update(id,data)
    return jsonify(json)

@app.route("/egresos/<string:id>",methods=['DELETE'])
def eliminarEgreso(id):
    json=miControladorEgreso.delete(id)
    return jsonify(json)

"""
metodo de relacion categoria  - Egresos
"""

@app.route("/egresos/<string:id>/categoria/<string:id_categoria>", methods=['PUT'])
def asignarCategoriaAEgreso(id, id_categoria):
    json = miControladorEgreso.asignarCategoria(id, id_categoria)
    return jsonify(json)






"-----------------------------------------------------------------------------"
"""
Servicio que el servidor ofrecerá, y este consiste en retornar un JSON el cual
tiene un mensaje que dice que el servidor está corriendo.
"""

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

"""
Método leer el archivo de configuración del proyecto,
retornará un diccionario el cual posee la información dentro del
JSON y se podrá acceder a los atributos necesarios.
"""
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    """
       Se crea la instancia del servidor con la url del backend y puerto especificado 
       en el archivo de configuración.
       """
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])