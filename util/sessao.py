# sessao.py

# - importações
import json
import os

usuario_atual = None # - variável global para armazenar o usuário atual da sessão

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # - diretório base do projeto
ARQUIVO = os.path.join(BASE_DIR, "dados", "sessao.json") # - caminho do arquivo de sessão

# - salvar sessão do usuário em um arquivo JSON
def salvar_sessao(usuario):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(
            {"usuario": usuario},
            arquivo,
            indent=4
        )

# - iniciar sessão do usuário e salvar em arquivo
def iniciar_sessao(usuario):
    global usuario_atual
    usuario_atual = usuario
    salvar_sessao(usuario)

# - carregar sessão do usuário a partir do arquivo JSON
def carregar_sessao():
    global usuario_atual

    if not os.path.exists(ARQUIVO): # - se o arquivo de sessão não existir, retorna None
        return None

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        usuario_atual = dados.get("usuario")

        return usuario_atual

    except (json.JSONDecodeError, OSError):
        return None

# - encerrar sessão do usuário e remover o arquivo JSON
def encerrar_sessao():
    global usuario_atual

    usuario_atual = None

    if os.path.exists(ARQUIVO): # - apagar o arquivo de sessão se ele existir
        os.remove(ARQUIVO)

# - obter o usuário atual da sessão
def obter_usuario():
    return usuario_atual

# - encerrar sessão do usuário
def encerrar_sessao():
    global usuario_atual
    usuario_atual = None