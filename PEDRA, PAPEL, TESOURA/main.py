import customtkinter as ctk
import random

def jogar(escolha_usuario):
    opcoes = ["Pedra", "Papel", "Tesoura"]
    escolha_pc = random.choice(opcoes)

    if escolha_usuario == escolha_pc:
        resultado = "Empate"
    elif (escolha_usuario == "Pedra" and escolha_pc == "Tesoura") or \
         (escolha_usuario == "Papel" and escolha_pc == "Pedra") or \
         (escolha_usuario == "Tesoura" and escolha_pc == "Papel"):
        resultado = "Você venceu!"
    else:
        resultado = "Você perdeu"

    label_resultado.configure(
        text=f"Jogador escolheu: {escolha_usuario}\n"
             f"Computador escolheu: {escolha_pc}\n\n"
             f"Resultado: {resultado}"
    )


janela = ctk.CTk()
janela.geometry("400x300")

titulo_game = ctk.CTkLabel(janela, text="Escolha sua jogada")
titulo_game.pack(pady=5)

btn_pedra = ctk.CTkButton(janela, text="Pedra", command=lambda: jogar("Pedra"))
btn_pedra.pack(pady=5)

btn_papel = ctk.CTkButton(janela, text="Papel", command=lambda: jogar("Papel"))
btn_papel.pack(pady=5)

btn_tesoura = ctk.CTkButton(janela, text="Tesoura", command=lambda: jogar("Tesoura"))
btn_tesoura.pack(pady=5)

label_resultado = ctk.CTkLabel(janela, text="", fg_color="black")
label_resultado.pack(pady=5)

janela.mainloop()