import tkinter as tk
from datetime import datetime

# Variaveis globais
janela = tk.Tk()
indice = 0 
cores = ["black", "white"]
afters = []

janela.configure(bg=cores[0])

janela.attributes("-fullscreen", True)



janela.config(cursor="none")

# Ajustando o mostrador da hora

hora = tk.Label(janela,text=datetime.now().strftime("%H:%M:%S"),fg="white", bg="black",
                  font=("Arial",30))
hora.pack()


rotulo = tk.Label(janela,text="Sirene interativa",fg="white", bg="black",
                  font=("Arial",40))
rotulo.pack(expand=True)


#Funções

def atualizar_hora():
    try:
    
        hora.config(text=datetime.now().strftime("%H:%M:%S"))
    
    except Exception as e:
        print(e)
    
    janela.after(1000, atualizar_hora)

def piscar():
    global indice
    
    try:
        janela.configure(bg=cores[indice])
                
        indice = 1 if indice == 0 else 0
        print(indice)
    
        
    except Exception as e:
        print(e)
    
    janela.after(500,piscar)

def fechar_janela(event):
    
    janela.destroy()
    

janela.bind("<Escape>", fechar_janela)


atualizar_hora()

piscar()

janela.mainloop()