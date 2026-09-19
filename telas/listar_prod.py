# listar_prod.py

# - importações
import customtkinter as ctk
from PIL import Image
from util.prod_save import carregar_meus_produtos, salvar_produtos
from util.cmds import botao_voltar_menu
from telas.menu import abrir_menu
import os
from util.cmds import carregar_imagem

# - abrir tela de listagem de produtos
def abrir_listar(janela):
    janela.title("Listar Produtos")

    # - frame principal
    frame = ctk.CTkScrollableFrame(
    janela,
    width=450,
    height=500,
    fg_color="transparent"
    )

    frame._scrollbar.grid_remove()

    titulo = ctk.CTkLabel(
    frame,
    text="Listar Produtos",
    font=("Segoe UI", 24, "bold")
    )
    titulo.pack(pady=20)

    erro_label = ctk.CTkLabel(
        frame,
        text="",
        font=("Helvetica", 20, "bold"),
        text_color="red"
    )

    produtos = carregar_meus_produtos() # - carregar produtos salvos

    if produtos: # - se houver produtos, criar cards para cada produto
        for produto in produtos:
            caixa_image = carregar_imagem("caixa.png", (50, 50))

            def editar_produto(p, j): # - função para editar produto
                from util.cmds import trocar_tela
                from telas.editar import abrir_editar_produto

                trocar_tela(j, lambda j: abrir_editar_produto(j, p))
            
            excluir_produto = lambda p, f, j: (
                produtos.remove(p),
                salvar_produtos(produtos),
                f.destroy(),
                abrir_listar(j)
            ) # - excluir produto

            card = ctk.CTkFrame(
                frame,
                corner_radius=10
            ) # - card para cada produto

            editar_produto_button = ctk.CTkButton(
                frame,
                text="Editar",
                command=lambda p=produto: editar_produto(p, janela),
                compound="right",
                fg_color="blue",
                hover_color="blue"
            )
            editar_produto_button.place(x=270, y=102)

            excluir_button = ctk.CTkButton(
                card,
                text="Excluir",
                command=lambda p=produto: excluir_produto(p, frame, janela),
                fg_color="red",
                hover_color="#ff4d4d"
            )
            excluir_button.place(x=260, y=78)

            caixa = ctk.CTkLabel(
                card,
                image=caixa_image,
                text="",
                width=50,
                height=50
            )
            caixa.pack(side="left", padx=10, pady=10)

            titulo = ctk.CTkLabel(
                card,
                compound="left",
                text=f"{produto['nome_produto']}",
                font=("Segoe UI", 18, "bold")
            )

            preco = ctk.CTkLabel(
                card,
                text=f"Preço: R${produto['preco']:.2f}"
            )

            quantidade = ctk.CTkLabel(
                card,
                text=f"Quantidade: {produto['quantidade']}"
            )

            titulo.pack(anchor="w", padx=15, pady=(10,5))
            preco.pack(anchor="w", padx=15)
            quantidade.pack(anchor="w", padx=15, pady=(0,10))

            card.pack(fill="x", padx=10, pady=8)
    
    if not produtos: # - se não existir produtos, mostrar mensagem 'você não tem produtos registrados'
        erro_label.configure(text="Você não tem produtos registrados!")


    erro_label.pack(pady=20)
    botao_voltar_menu(frame, janela, abrir_menu)

    frame.pack(pady=20)