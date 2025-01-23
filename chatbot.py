from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

# Instanciando o modelo
chat = ChatGroq(model='llama-3.3-70b-versatile')

def resposta_bot(mensagens, documentos):
    mensagem_modelo = [
        ('system', '''Você é um técnico que atua no CIEVS Roraima. Você é profundo conhecedor das definicções que envolvem o CIEVS tanto a nível nacional
        como estadual. Responda as perguntas de forma cordial e profissional. Caso não tenha a resposta ao que foi perguntado, deverá solicitar que o usuário 
        entre em contato com o CIEVS-Roraima via e-mail. As respostas deverão ser baseadas nos seguintes documentos {documentos_informados}.''')
    ]
    mensagem_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagem_modelo)
    chain = template | chat

    # Obter a última mensagem do usuário
    input_usuario = mensagens[-1][1] if mensagens else ""

    return chain.invoke({'documentos_informados': documentos, 'input': input_usuario}).content
