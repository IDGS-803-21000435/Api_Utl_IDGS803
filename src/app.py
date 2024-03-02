from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

from config import config

app = Flask(__name__)
con = MySQL(app)

@app.route('/alumnos', methods=["GET"])
def listar_alumnos():
    try:
        cursor = con.connection.cursor()
        sql = "select*from alumnos"
        cursor.execute(sql)
        datos = cursor.fetchall()
        alumnos = []
        for fila in datos:
            alumnos = {
                'matricula': fila[0],
                'nombre': fila[1],
                'apaterno':fila[2],
                'amaterno': fila[3],
                'correo': fila[4]
            }
            
            alumnos.append(alumnos)
        return jsonify({
            'alumnos':alumnos,
            'mensaje': 'Lista de alumnos',
            'exito': True
        })
        
    except Exception as ex:
        return jsonify({
            'mensaje':'error {}'.format(ex),
            'exito': False
        })