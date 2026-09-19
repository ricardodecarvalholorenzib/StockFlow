# banco_data.py

# - importações
import json
from util.seguranca import criptografar_senha
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # - diretório base do projeto
ARQUIVO = os.path.join(BASE_DIR, "dados", "usuarios.json") # - caminho do arquivo de usuários


# - carregar usuários do arquivo JSON
def carregar_usuarios():
    with open(ARQUIVO, "r", encoding="utf-8") as f: # - abrir o arquivo de usuários em modo leitura
        return json.load(f)

# - salvar usuários no arquivo JSON
def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w", encoding="utf-8") as f: # - abrir o arquivo de usuários em modo escrita
        json.dump(usuarios, f, indent=4, ensure_ascii=False)

# - verificar se o usuário existe no arquivo JSON
def usuario_existe(usuario):
    usuarios = carregar_usuarios() # - carregar a lista de usuários do arquivo JSON

    # verificar se o usuário existe na lista de usuários (ignorando maiúsculas e minúsculas)
    return any(
        u["usuario"].lower() == usuario.lower()
        for u in usuarios
    )


# - criar um novo usuário e salvar no arquivo JSON
def criar_usuario(usuario, senha):

    if usuario_existe(usuario): # - se o usuário já existir, retorna False
        return False

    usuarios = carregar_usuarios() # - carregar a lista de usuários do arquivo JSON

    usuarios.append({
        "usuario": usuario,
        "senha": criptografar_senha(senha)
    }) # - adicionar o novo usuário à lista de usuários

    salvar_usuarios(usuarios)

    return True


# - autenticar usuário verificando se o usuário e senha correspondem a um registro no arquivo JSON
def autenticar_usuario(usuario, senha):

    senha = criptografar_senha(senha) # - criptografar a senha fornecida para comparação com a senha armazenada

    usuarios = carregar_usuarios() # - carregar a lista de usuários do arquivo JSON

    return any(
        u["usuario"] == usuario and
        u["senha"] == senha
        for u in usuarios
    ) # - retorna True se o usuário e senha correspondem a um registro no arquivo JSON, caso contrário, retorna False