import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Vulnerabilidad: Exposición de información sensible (Hardcoded Secrets)
API_KEY = {{secrets.TOKEN}}

# Inicializa una base de datos en memoria con algunos datos ficticios
def init_db():
    conn = sqlite3.connect(':memory:')
    conn.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)''')
    conn.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')")
    conn.execute("INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com')")
    conn.commit()
    return conn

# Ruta vulnerable a Inyección de Comandos
@app.route('/exec')
def exec_command():
    cmd = request.args.get('cmd')
    
    # Vulnerabilidad: Inyección de Comandos, ejecuta cualquier comando del sistema
    result = os.popen(cmd).read()
    
    return f"Resultado del comando: <pre>{result}</pre>"

# Ruta vulnerable a Inyección SQL
@app.route('/users')
def get_user():
    user_id = request.args.get('id')
    
    # Vulnerabilidad: Inyección SQL, no se sanitiza el parámetro 'user_id'
    conn = init_db()
    cursor = conn.execute(f"SELECT * FROM users WHERE id = {user_id}")
    result = cursor.fetchall()
    
    return f"Resultado de la búsqueda: {result}"

# Ruta vulnerable a Exposición de Información Sensible
@app.route('/')
def index():
    return f"The API Key is: {API_KEY}"

# Ruta vulnerable a Cross-Site Scripting (XSS)
@app.route('/search')
def search():
    query = request.args.get('query')
    
    # Vulnerabilidad: XSS, no se sanitiza el input del usuario
    return f"<h1>Resultados para: {query}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
