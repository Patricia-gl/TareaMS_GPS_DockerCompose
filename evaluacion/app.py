from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="hola",
        database="dbbtarea"
    )

@app.route('/evaluacion', methods=["POST"])
def crear_evaluacion():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiante WHERE rut = %s", (data["rut"],))
    if cursor.fetchone() is None:
        conn.close()
        return jsonify({"message": "Estudiante no existe"}), 400
    cursor.execute("INSERT INTO evaluacion (rut, semestre, asignatura, nota) VALUES (%s, %s, %s, %s)", (data["rut"], data["semestre"], data["asignatura"], data["nota"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Evaluacion creada"}), 200

@app.route('/evaluacion', methods=["GET"])
def listar_evaluaciones():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM evaluacion")
    evaluaciones = cursor.fetchall()
    conn.close()
    return jsonify(evaluaciones), 200

@app.route('/evaluacion/<rut>', methods=["GET"])
def evaluaciones_por_rut(rut):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM evaluacion WHERE rut = %s", (rut,))
    evaluacioes = cursor.fetchall()
    conn.close()
    return jsonify(evaluacioes), 200
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3001)


