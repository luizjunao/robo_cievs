from langchain_community.document_loaders import PyPDFLoader

def carregar_documento(caminho_arquivo):
    loader = PyPDFLoader(caminho_arquivo)
    lista_documentos = loader.load()
    documento = ''.join([doc.page_content for doc in lista_documentos])
    return documento
