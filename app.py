from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__) # Permitir requisições do frontend
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    # 1. Receber a mensagem do frontend
    user_message = request.json.get('message').lower()

    # 2. Processar a resposta
    response = get_chatbot_response(user_message)

    # 3. Enviar a resposta de volta ao frontend
    return jsonify({'response': response})

def get_chatbot_response(message):
    # Simulação das nossas intenções Acadêmicas

    if 'olá' in message or 'bom dia' in message or 'oi' in message or 'boa tarde' in message or 'boa noite' in message or 'Eddie' in message: 
        return 'Olá! Eu sou o Eddie, seu assistente acadêmico. Como posso ajudar você hoje? (Faça perguntas sobre horários, matrícula)'
    
    elif "horário" in message or "aulas" in message:
        return "Para a semana, você tem as seguintes aulas: Cálculo (Seg 10h), Programação (Ter 14h) e Projeto (Qui 9h)."

    elif "nota" in message or "média" in message:
        return "A sua nota final em 'Programação' foi 16. As notas de 'Projeto' ainda não foram lançadas. Deseja consultar mais alguma nota?"

    elif "matrícula" in message or "matricular" in message:
        return "O processo de matrícula para o próximo semestre estará aberto de 1 a 15 de Fevereiro. Consulte o portal do aluno para mais detalhes."

    elif "atestado" in message or "documento" in message:
        return "Pode solicitar seu atestado de frequência diretamente no portal do aluno, na secção 'Serviços Acadêmicos'. O prazo de emissão é de 3 dias úteis."
        
    else:
        return "Desculpe, não entendi a sua pergunta. Pode reformular ou perguntar sobre Horários, Notas, Matrícula ou Atestado?"

if __name__ == '__main__':
    # Roda o servidor na porta 5000 (Posso ajustar)
    app.run(debug=True, port=5000)