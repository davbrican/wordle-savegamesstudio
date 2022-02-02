from cv2 import repeat
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_cors.core import try_match
import os


app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


#Testing Route
@app.route('/', methods=['GET'])
def getDefault():
    return jsonify({'response': 'Hello to my users api!'})


def test_palabra(entrada, numero_intentos):
    res = []
    if numero_intentos < 6:
        palabra = "spidey"
        
        if len(entrada) != len(palabra):
            return "Tamaño de palabra incorrecto (tamaño correcto: "+str(len(palabra))+")"

        repeticiones_entrada = {}
        repeticiones_palabra = {}
        codigo_de_colores = ["gris", "naranja", "verde"]

        for i in range(len(entrada)):
            letra = entrada[i]
            letra_palabra = palabra[i]
            
            if letra not in repeticiones_entrada:
                repeticiones_entrada[letra] = 1
            else: 
                repeticiones_entrada[letra] += 1
                
            if letra_palabra not in repeticiones_palabra:
                repeticiones_palabra[letra_palabra] = 1
            else: 
                repeticiones_palabra[letra_palabra] += 1
                    
            if letra == letra_palabra:
                res.append(codigo_de_colores[2])
            elif letra in palabra:
                res.append(codigo_de_colores[1])
            else:
                res.append(codigo_de_colores[0])
                
        for j in range(len(entrada)):
            if entrada[j] in repeticiones_palabra and repeticiones_entrada[entrada[j]] > repeticiones_palabra[entrada[j]] and res[j] != codigo_de_colores[2]:
                repeticiones_entrada[entrada[j]] -= 1
                res[j] = codigo_de_colores[0]
            
        numero_intentos += 1
        
        return res
    else:
        return res
    
    
#Create Workers Routes
@app.route('/testWord', methods=['POST'])
def testWord():
    #mysql data
    palabra = request.json['palabra']
    numero_intentos = request.json['numero_intentos']
    
    res = test_palabra(palabra, numero_intentos)
    return jsonify({'result': res})


if __name__ == '__main__':
    app.run(debug=True, port=8000)