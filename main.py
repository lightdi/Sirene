import tkinter as tk

janela = tk.Tk()



janela.configure(bg="black")

janela.attributes("-fullscreen", True)



janela.config(cursor="none")


rotulo = tk.Label(janela,text="Sirene interativa",fg="white", bg="black",
                  font=("Arial",40))
rotulo.pack(expand=True)


def fechar_janela(event):
    janela.destroy()
    
    
janela.bind("<Escape>", fechar_janela)


janela.mainloop()