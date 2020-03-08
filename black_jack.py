from random import randint as r


class Blackjack():

    black_jack_cards = [
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


    def __init__(self, card = {'numero': '0', 'suit': 'None'}):
        self.card = card


    def get_card(self):
        return self.card


    def set_card(self, x: dict):
        self.card = x


    def pick_card(self):
        indice_card = r(0,len(self.black_jack_cards)-1)
        print(len(self.black_jack_cards))
        return self.black_jack_cards.pop(indice_card)

eu = Blackjack()
while True:
    opt = input('Pressione 1 para pegar uma carta e 0 para sair:')
    if opt.lower().strip() == '1':
        print(f'A carta sorteada foi {eu.pick_card()}')
    else:
        break
