import requests
from flask import Flask,request
from flask_api import status

app = Flask(__name__)

def controller_poker(headers):

    try:
        # ! Asignamos los headers a una variable correspondiente
        poke_url = headers['endpoint_poke_api']
        exists_ability = headers['ability_name']
        index_ability = headers['index_ability']

        index_ability = int(index_ability)
        response = requests.get(poke_url) 
        response = response.json()

        abilities = response['abilities'][index_ability]
        ability_name = abilities['ability']['name']

    except Exception as e:
        return {'error': e.args[0]}, 400
    else:
        if exists_ability in ability_name:
            return {'exists_ability_name': True},200
        
        return {'exists_ability_name': False}, 200

@app.route("/pokemon")
def poke():
    response = controller_poker(request.headers)
    return response

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000, debug=True)