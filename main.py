import tkinter as tk
from datetime import datetime

janela = tk.Tk()



janela.configure(bg="black")

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
    
    hora.config(text=datetime.now().strftime("%H:%M:%S"))
    
    janela.after(1000, atualizar_hora)



def fechar_janela(event):
    janela.destroy()
    

janela.bind("<Escape>", fechar_janela)


atualizar_hora()

janela.mainloop()