import random, json
from flask import Flask

app = Flask(__name__)

class Blackjack():


    def __init__(self):
        self.card = [
    {'number': '1', 'suit': 'Ouro'},
    {'number': '2', 'suit': 'Ouro'},
    {'number': '3', 'suit': 'Ouro'},
    {'number': '4', 'suit': 'Ouro'},
    {'number': '5', 'suit': 'Ouro'},
    {'number': '6', 'suit': 'Ouro'},
    {'number': '7', 'suit': 'Ouro'},
    {'number': '8', 'suit': 'Ouro'},
    {'number': '9', 'suit': 'Ouro'},
    {'number': '10', 'suit': 'Ouro'},
    {'number': '11', 'suit': 'Ouro'},
    {'number': '12', 'suit': 'Ouro'},
    {'number': '13', 'suit': 'Ouro'},
    {'number': '1', 'suit': 'Espadas'},
    {'number': '2', 'suit': 'Espadas'},
    {'number': '3', 'suit': 'Espadas'},
    {'number': '4', 'suit': 'Espadas'},
    {'number': '5', 'suit': 'Espadas'},
    {'number': '6', 'suit': 'Espadas'},
    {'number': '7', 'suit': 'Espadas'},
    {'number': '8', 'suit': 'Espadas'},
    {'number': '9', 'suit': 'Espadas'},
    {'number': '10', 'suit': 'Espadas'},
    {'number': '11', 'suit': 'Espadas'},
    {'number': '12', 'suit': 'Espadas'},
    {'number': '13', 'suit': 'Espadas'},
    {'number': '1', 'suit': 'Copas'},
    {'number': '2', 'suit': 'Copas'},
    {'number': '3', 'suit': 'Copas'},
    {'number': '4', 'suit': 'Copas'},
    {'number': '5', 'suit': 'Copas'},
    {'number': '6', 'suit': 'Copas'},
    {'number': '7', 'suit': 'Copas'},
    {'number': '8', 'suit': 'Copas'},
    {'number': '9', 'suit': 'Copas'},
    {'number': '10', 'suit': 'Copas'},
    {'number': '11', 'suit': 'Copas'},
    {'number': '12', 'suit': 'Copas'},
    {'number': '13', 'suit': 'Copas'},
    {'number': '1', 'suit': 'Paus'},
    {'number': '2', 'suit': 'Paus'},
    {'number': '3', 'suit': 'Paus'},
    {'number': '4', 'suit': 'Paus'},
    {'number': '5', 'suit': 'Paus'},
    {'number': '6', 'suit': 'Paus'},
    {'number': '7', 'suit': 'Paus'},
    {'number': '8', 'suit': 'Paus'},
    {'number': '9', 'suit': 'Paus'},
    {'number': '10', 'suit': 'Paus'},
    {'number': '11', 'suit': 'Paus'},
    {'number': '12', 'suit': 'Paus'},
    {'number': '13', 'suit': 'Paus'}
        ]
    @app.route('/', methods=['GET'])
    def get_cards():
        cartas = Blackjack()
        lista = random.choices(cartas.card, k= len(cartas.card))
        return json.dumps(lista)

app.run(host='localhost', port=8080, debug=True)