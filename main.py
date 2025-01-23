import streamlit as st
import config  # Importar o config.py para configurar a API
from chatbot import resposta_bot
from doc_loader import carregar_documento

# Carregando documentos
documento = carregar_documento('CIEVS.pdf')

# Configuração do layout no Streamlit
st.set_page_config(page_title="Chatbot CGVS", layout="wide")
st.title("Chatbot do CIEVS-Roraima")

# Inicializa o estado da sessão
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": 'Olá. Sou o atendente virtual do *CIEVS-Roraima*. Em que posso te ajudar hoje?'}
    ]

# Função para processar a entrada do usuário
def process_user_input():
    if st.session_state["user_input"]:
        # Adiciona a mensagem do usuário ao histórico
        st.session_state["messages"].append({"role": "user", "content": st.session_state["user_input"]})

        # Gera a resposta do bot
        mensagens = [(msg["role"], msg["content"]) for msg in st.session_state["messages"]]
        bot_response = resposta_bot(mensagens, documento)

        # Adiciona a resposta do bot ao histórico
        st.session_state["messages"].append({"role": "assistant", "content": bot_response})

        # Limpa o campo de entrada de texto
        st.session_state["user_input"] = ""

# Exibindo o histórico de conversa acima
st.write("### Histórico de conversa")
chat_placeholder = st.empty()
with chat_placeholder.container():
    for message in st.session_state["messages"]:
        if message["role"] == "assistant":
            st.markdown(f"**🤖 CIEVS-Roraima:** {message['content']}")
        else:
            st.markdown(f"**🧑 Você:** {message['content']}")

# Caixa de texto fixa na parte inferior
st.write("---")  # Linha divisória
user_input = st.text_input(
    "Digite sua mensagem aqui:",
    key="user_input",
    on_change=process_user_input,
    placeholder="Escreva sua mensagem e pressione Enter..."
)
