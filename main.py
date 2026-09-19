# main.py

import customtkinter as ctk

ctk.set_appearance_mode("light")

# ==========================================
# IMPORT JANELA CRIAR CONTA
# ==========================================

from telas.acc_create import criar_conta

janela = ctk.CTk()

janela.title("StockFlow | Criar Conta")
janela.geometry("600x600")

criar_conta(janela)

janela.mainloop()