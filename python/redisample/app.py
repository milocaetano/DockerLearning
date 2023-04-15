from flask import Flask, jsonify
import redis

app = Flask(__name__)

# Crie uma conexão com o Redis
r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def hello():
    # Defina uma chave e valor no Redis
    r.set('mykey', 'Hello, Redis!')

    # Obtenha o valor da chave no Redis
    value = r.get('mykey')

    # Retorne o valor como uma resposta HTTP
    return value.decode('utf-8')

@app.route('/helloworld')
def hello_world():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
