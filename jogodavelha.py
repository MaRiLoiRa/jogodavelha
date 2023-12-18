import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Jogo da Velha")
        self.jogador_atual = "X"
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]

        # Configurando os botões
        self.botoes = [[tk.Button(self.janela, text="", font=("Helvetica", 24), width=5, height=2, command=lambda r=r, c=c: self.clique(r, c)) for c in range(3)] for r in range(3)]
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].grid(row=i, column=j)

    def clique(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == "":
            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.botoes[linha][coluna].config(text=self.jogador_atual)

            if self.verificar_vitoria():
                messagebox.showinfo("Fim do Jogo", f"Jogador {self.jogador_atual} venceu!")
                self.reiniciar_jogo()
            elif self.verificar_empate():
                messagebox.showinfo("Fim do Jogo", "O jogo terminou em empate!")
                self.reiniciar_jogo()
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def verificar_vitoria(self):
        # Verifica linhas, colunas e diagonais
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != "":
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != "":
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != "":
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != "":
            return True
        return False

    def verificar_empate(self):
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == "":
                    return False
        return True

    def reiniciar_jogo(self):
        for i in range(3):
            for j in range(3):
                self.tabuleiro[i][j] = ""
                self.botoes[i][j].config(text="")
        self.jogador_atual = "X"

    def iniciar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.iniciar()
