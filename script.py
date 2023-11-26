import tkinter as tk
import re
import random

def Iniciar():
    JanelaInicial = tk.Tk()
    JanelaInicial.title("Menu")
    Largura = 250
    Altura = 135
    JanelaInicial.geometry(f"{Largura}x{Altura}")
    
    BotaoFacil = tk.Button(JanelaInicial, text="Fácil", command=lambda: IniciarJogo(dificuldade=1, janelaInicial=JanelaInicial), padx=50, pady=10, bg="green")
    BotaoMedio = tk.Button(JanelaInicial, text="Médio", command=lambda: IniciarJogo(dificuldade=2, janelaInicial=JanelaInicial), padx=50, pady=10, bg="yellow")
    BotaoDificil = tk.Button(JanelaInicial, text="Dificil", command=lambda: IniciarJogo(dificuldade=3, janelaInicial=JanelaInicial), padx=50, pady=10, bg="red")
    
    BotaoFacil.pack()
    BotaoMedio.pack()
    BotaoDificil.pack()
    
    JanelaInicial.mainloop()
    
def IniciarJogo(dificuldade, janelaInicial):
    print("Jogo inciciado de dificuldade " + str(dificuldade))
    janelaInicial.destroy()
    
    NumeroAleatoriamenteGerado = 0
    
    if dificuldade == 1:
        NumeroAleatoriamenteGerado = random.randint(0, 10)
    elif dificuldade == 2:
        NumeroAleatoriamenteGerado = random.randint(0, 20)
    elif dificuldade == 3:
        NumeroAleatoriamenteGerado = random.randint(0, 30)
    
    print("Foi gerado:" + str(NumeroAleatoriamenteGerado))
    
    JanelaJogo = tk.Tk()
    JanelaJogo.title("Tente adivinhar")
    Largura = 250
    Altura = 135
    JanelaJogo.geometry(f"{Largura}x{Altura}")

    entrada = tk.Entry(JanelaJogo)
    entrada.pack()
    BotaoConfirmar = tk.Button(JanelaJogo, text="Confirmar", bg="green", padx=50, pady=10, command=lambda: Confirmar(entrada=entrada.get(), numeroGerado=NumeroAleatoriamenteGerado, JanelaJogo=JanelaJogo))
    BotaoConfirmar.place(y=50, x=50)

    JanelaJogo.mainloop()

def AcharNumeros(numeroColocado):
    padrao = re.compile(r'\d+')
    numeros_encontrados = padrao.findall(numeroColocado)
    return numeros_encontrados
    
def Confirmar(entrada, numeroGerado, JanelaJogo):
    Numero = AcharNumeros(entrada)
    
    JanelaJogo.destroy()
    Largura = 250
    Altura = 135
    if int(Numero[0]) == numeroGerado:        
        JanelaGanhou = tk.Tk()
        JanelaGanhou.title("Ganhou")
        JanelaGanhou.geometry(f"{Largura}x{Altura}")
        Texto = tk.Label(JanelaGanhou, text="Você ganhou!!", font=("Arial", 20, "bold"), fg="green")
        Texto.pack()
        
        JanelaGanhou.mainloop()
    else:
        JanelaPerdeu = tk.Tk()
        JanelaPerdeu.title("Perdeu")
        JanelaPerdeu.geometry(f"{Largura}x{Altura}")
        Texto = tk.Label(JanelaPerdeu, text=f"Você perdeu!\nO número era: {numeroGerado}", font=("Arial", 20, "bold"), fg="red")
        Texto.pack()
        
        JanelaPerdeu.mainloop()
        
Iniciar()