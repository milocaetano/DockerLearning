from flask import Flask, jsonify, request
import redis

app = Flask(__name__)

# Crie uma conexão com o Redis

r = redis.Redis(host='redis', port=6379, db=0)


@app.route('/')
def hello():
     return jsonify({'message': 'Hello, Python'})
@app.route('/getredis')
def getredis():
    # Obtenha o valor da chave no Redis
    value = r.get('mykey')

    # Verifique se o valor é None antes de tentar decodificá-lo
    if value == None:
        return "Chave 'mykey' não encontrada no Redis"
    else:
        # Retorne o valor como uma resposta HTTP
        return value.decode('utf-8')


@app.route('/add')
def add():

    name = request.args.get('name')
    
    if name is not None:
        r.set('mykey', name)
    else:
        return jsonify({'message': 'Não foi possível adicionar o valor'}) 

    return jsonify({'message': 'Valor salvo com sucesso'}) 

@app.route('/helloworld')
def hello_world():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
