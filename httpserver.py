from flask import Flask, request,abort

app = Flask(__name__)
seed = 0
HTTP_OK=200

@app.route('/', methods=['POST'])
def update_seed():
    global seed
    # Get data in json format
    if not request.is_json:
        abort(400)
    data = request.get_json()
    num = data.get('num')
    # Process Post request
    if type(num) == int:
        seed = num
    else:
        abort(400)
    reponse_msg = f"Seed updated to {seed} successfully!"
    status_code = HTTP_OK
    return "OK"


@app.route('/', methods=['GET'])
def get_seed():
    reponse_msg = str(seed)
    status_code = HTTP_OK
    return reponse_msg

if __name__ == '__main__':
    app.run(host="0.0.0.0",
            port=5000)
