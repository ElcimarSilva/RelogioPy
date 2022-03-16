from tkinter import *
import datetime


def infos_no_print():
    data_public = datetime.datetime.now()
    data_public_str = data_public.strftime("%m/%d/%Y %H:%M:%S")
    texto_do_metodo["text"] = data_public_str


janela = Tk()
janela.title("Minha janela criada em Python")
# janela.geometry("400x400")

texto_orientacao = Label(janela, text="Clique para atualizar data e hora")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Atualizar", command=infos_no_print)
botao = botao.grid(column=0, row=3, padx=10, pady=10)

texto_do_metodo = Label(janela, text="")
texto_do_metodo.grid(column=0, row=5, padx=10, pady=10)

janela.mainloop()
