from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)
HTTP_OK=200
@app.route('/', methods=['POST'])
def run_stress_cpu():
    subprocess.Popen(['python3', 'stress_cpu.py'])
    return "OK"


@app.route('/', methods=['GET'])
def get_privateIP():
    privateip = socket.gethostbyname(socket.gethostname())
    return privateip

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
