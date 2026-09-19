# login.py

# - importações
import customtkinter as ctk
from telas.menu import abrir_menu
from PIL import Image
from util.cmds import carregar_imagem
import os
from util.banco_data import autenticar_usuario
from util.sessao import iniciar_sessao

def abrir_login(janela):
    janela.title("Entrar em uma Conta | StockFlow")

    # - frame
    frame = ctk.CTkFrame(
        janela,
        width=600,
        height=600,
        corner_radius=10,
        fg_color="transparent"
    )
    frame.pack(expand=True)

    # - corpo do login
    titulo = ctk.CTkLabel(
        frame,
        text="🔑 Entrar no StockFlow",
        font=("Segoe UI", 45, "bold"),
        text_color="grey"
    )
    titulo.pack(pady=(0, 30))

    nome_login = ctk.CTkEntry(
        frame,
        placeholder_text="Usuário",
        width=300,
        height=40
    )
    nome_login.pack(pady=10)

    frame_senha = ctk.CTkFrame(frame, fg_color="transparent")
    frame_senha.pack(pady=10)

    senha_login = ctk.CTkEntry(
        frame_senha, 
        placeholder_text="Senha", 
        show="*",
        width=243,
        height=40
    )
    senha_login.pack(side="left", padx=(0, 10))
    
    eye = carregar_imagem("eyes_on.png", (30, 20))
    eye_off = carregar_imagem("eyes_off.png", (30, 24))
    
    mostrando = False
    
    def mostrar_senha():
        nonlocal mostrando
        mostrando = not mostrando
        if mostrando:
            senha_login.configure(show="") 
            botao_olho.configure(image=eye_off) 
        else: 
            senha_login.configure(show="*") 
            botao_olho.configure(image=eye) 
        
    botao_olho = ctk.CTkButton(
        frame_senha,
        image=eye,
        text="",
        width=40,
        height=40,
        fg_color="transparent",
        hover=False,
        command=mostrar_senha
    )
    botao_olho.pack(side="left")

    erro_label = ctk.CTkLabel(
        frame,
        text="",
        font=("Segoe UI", 15),
        text_color="red"
    )
    erro_label.pack(pady=5)

    check_manter_login = ctk.CTkCheckBox(
        frame,
        text="Manter-me conectado",
        font=("Segoe UI", 13)
    )
    check_manter_login.pack(pady=10)

    botao_login = ctk.CTkButton(
        frame,
        text="Entrar",
        font=("Segoe UI", 20),
        text_color="white",
        width=200,
        height=45
    )
    botao_login.pack(pady=(20, 0))

    def criar_conta():
        from util.cmds import trocar_tela
        from telas.acc_create import criar_conta

        trocar_tela(janela, criar_conta)

    botao_criar_conta = ctk.CTkButton(
    frame,
    text="Não possui uma Conta?\nCriar conta",
    fg_color="transparent",
    hover=False,
    text_color="#1E90FF",
    font=("Segoe UI", 13, "underline"),
    command=criar_conta
    )
    botao_criar_conta.pack(pady=20)
    # - fim do corpo do login

    # - função de cadastro
    def cadastro():

        usuario = nome_login.get().strip()
        senha = senha_login.get()

        if not usuario:
            erro_label.configure(text="Digite seu usuário.") # - se o campo de usuário estiver vazio, exibe uma mensagem de erro
            return

        if not senha:
            erro_label.configure(text="Digite sua senha.") # - se o campo de senha estiver vazio, exibe uma mensagem de erro
            return
        
        if autenticar_usuario(usuario, senha): # - se o usuário e senha estiverem corretos, inicia a sessão e abre o menu
            
            iniciar_sessao(usuario)

            from util.cmds import trocar_tela

            trocar_tela(janela, abrir_menu)
        else:
            erro_label.configure(text="Usuário ou senha incorretos.") # - se o usuário ou senha estiverem incorretos, exibe uma mensagem de erro

    botao_login.configure(command=cadastro)