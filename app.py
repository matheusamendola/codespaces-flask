from flask import Flask, request
import random

app = Flask(__name__)

# Lista de mensagens de horóscopo
horoscope_messages = [
    'A sorte está ao seu lado hoje.',
    'Prepare-se para grandes desafios.',
    'Um novo amor está prestes a entrar em sua vida.',
    'Seja paciente e perseverante nos seus objetivos.',
    'Evite tomar decisões impulsivas.',
    'Foque nas suas metas e alcance o sucesso.',
    'Um amigo próximo vai lhe oferecer ajuda.',
    'Seja grato pelas pequenas coisas na vida.'
]

# Rota para receber as informações do signo e retornar a mensagem do dia
@app.route('/horoscope', methods=['GET'])
def get_horoscope():
    sign = request.json['sign']
    plan = request.json['plan']

    # Gera uma mensagem de horóscopo aleatória
    message = random.choice(horoscope_messages)

    horoscope = {
        'sign': sign,
        'message': message,
    }

    # Verifica o tipo de plano e adiciona recursos específicos
    if plan == 'basic':
        horoscope['lucky_number'] = None  # Não fornece número da sorte
    elif plan == 'advanced':
        horoscope['lucky_number'] = random.randint(1, 10)  # Número da sorte aleatório entre 1 e 10
        horoscope['lucky_animal'] = random.choice(['Gato', 'Cachorro', 'Leão', 'Tigre', 'Girafa'])  # Animal da sorte aleatório
    else:
        return {'error': 'Plano inválido.'}, 400

    return horoscope