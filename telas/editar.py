# editar.py

# - importações
import customtkinter as ctk
from util.prod_save import carregar_produtos, salvar_produtos

# - abrir janela de editar produtos
def abrir_editar_produto(janela, produto):

    janela.title("Editar Produto")

    # - frame principal
    frame = ctk.CTkScrollableFrame(
        janela,
        width=450,
        height=500,
        fg_color="transparent"
    )

    titulo = ctk.CTkLabel(
        frame,
        text="Editar Produto",
        font=("Segoe UI", 24, "bold")
    )
    titulo.pack(pady=20)

    error_label = ctk.CTkLabel(
        frame,
        text="",
        font=("Helvetica", 15),
        text_color="red"
    )

    error_label.pack(pady=5)

    nome_produto = ctk.CTkEntry(
        frame,
        placeholder_text="Nome do produto",
        width=300
    )
    nome_produto.pack(pady=10)

    preco_produto = ctk.CTkEntry(
        frame,
        placeholder_text="Preço do Produto",
        width=300
    )
    preco_produto.pack(pady=10)

    quantidade_produto = ctk.CTkEntry(
        frame,
        placeholder_text="Quantidade do Produto",
        width=300
    )
    quantidade_produto.pack(pady=10)

    nome_produto.insert(0, produto["nome_produto"])
    preco_produto.insert(0, str(produto["preco"]))
    quantidade_produto.insert(0, str(produto["quantidade"]))

    def salvar_edicao(): # - função de salvar edição do produto
        try:
            preco = float(
                preco_produto.get().replace(",", ".")
            )
            quantidade = int(
                quantidade_produto.get()
            )

        except ValueError: # - se os valores digitados não forem compátiveis, retorna erro
            error_label.configure(
                text="Digite valores válidos para preço e quantidade."
            )
            return

        novo_nome = nome_produto.get().strip()

        if not novo_nome: # - se o nome não for inserido, retorna erro
            error_label.configure(
                text="Digite o nome do produto."
            )
            return

        produtos = carregar_produtos() # - carrega os produtos

        for p in produtos:
            if (
                p["nome_produto"] == produto["nome_produto"]
                and p["usuario"] == produto["usuario"]
            ):
                p["nome_produto"] = novo_nome
                p["preco"] = preco
                p["quantidade"] = quantidade
                break

        salvar_produtos(produtos) # - salva os produtos

        from telas.menu import abrir_menu
        from util.cmds import trocar_tela

        trocar_tela(janela, abrir_menu)

    botao_salvar = ctk.CTkButton(
        frame,
        text="Salvar",
        command=salvar_edicao,
        fg_color="green",
        hover_color="#4dff4d"
    )
    botao_salvar.pack(pady=20)

    frame.pack(pady=20)