import React, { useState } from "react";
import axios from 'axios';
import './App.css';

function App() {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([{ text: "Olá! Sou o Eddie o seu assistente acadêmico. Como posso ajudar?", sender: 'bot' }
  ]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    //Função para adicionar a mensagem do usuário na tela
    const newMessages = [...messages, { text: input, sender: 'user' }];
    setMessages(newMessages);
    setInput('');

    try {
      // Chamada do servidor Flask
      const response = await axios.post('http://127.0.0.1:5000/chat', { message: input });

      // Função para adicionar a menssagem do bot na tela
      setMessages([...newMessages, { text: response.data.response, sender: 'bot' }]);
    } catch (error) {
      console.error("Erro ao conectar com o servidor:", error);
      setMessages([...newMessages, { text: "Erro: O servidor está desligado.", sender: 'bot' }]);
    }
  };

  return (
    <div className="chat-container">
      <h3 style={{ textAlign: 'center', color: '#007bff' }}>Chat bot para Atendimento Académico</h3>
      <div className="chat-window">
      {messages.map((msg, index) => (
        <div key={index} className={`message ${msg.sender}`}>
          {msg.text}
        </div>
      ))}
      </div>
      <div className="input-area">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
          placeholder="Digite alguma coisa..."
          />
          <button onClick={sendMessage}>Enviar</button>
      </div>
    </div>
  );
}

export default App;