from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OPENPLC_IP = "http://localhost:8080"  # OpenPLC'nin çalıştığı yer

def send_openplc_command(endpoint, data=None):
    url = f"{OPENPLC_IP}/{endpoint}"
    if data:
        response = requests.post(url, json=data)
    else:
        response = requests.get(url)
    return response.json()

@app.route('/set_input', methods=['POST'])
def set_input():
    data = request.json
    send_openplc_command("api/set_input", data)
    return jsonify({"message": "Giriş ayarlandı!"})

@app.route('/get_outputs', methods=['GET'])
def get_outputs():
    outputs = send_openplc_command("api/get_outputs")
    return jsonify(outputs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
