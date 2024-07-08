from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

some_data = { "name": "Bobby", "lastname": "Rixer" }
todos = [
    {"label":"My first task","done": False},
    {"label":"My second task","done":False}
]

@app.route('/todos', methods=['GET'])
def hello():
    jsn_text = jsonify(todos)
    return jsn_text


@app.route('/myroute', methods=['GET'])
def hello_world():
   json_text = jsonify(some_data)
   return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("You'll be destroyed:", position)
    todos.pop(position)
    return jsonify(todos)






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)