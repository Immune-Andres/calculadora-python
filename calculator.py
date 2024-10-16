from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form method="POST" action="/run">
            Command: <input name="cmd">
            <input type="submit">
        </form>
    '''

@app.route('/run', methods=['POST'])
def run():
    cmd = request.form['cmd']
    result = os.popen(cmd).read()  # Vulnerable a inyección de comandos
    return f'Result: {result}'

if __name__ == '__main__':
    app.run(debug=True)
