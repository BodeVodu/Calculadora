from tkinter import *
from tkinter import ttk


# cores

cor1 = '#010508'  # preto
cor2 = '#79b9d9'  # azul
cor3 = '#ebf2f5'  # branco
cor4 = '#f28305'  # laranja
cor5 = '#878584'  # cinza

janela = Tk()
janela.title("Calculadora")
janela.geometry("320x426")
janela.config(background=cor1)


frame_corpo = Frame(janela, width=320, height=525, bg=cor3)
frame_corpo.grid(row=1, column=0)

frame_tela = Frame(janela, width=320, height=75, bg=cor2)
frame_tela.grid(row=0, column=0,)


# variável valores

valores = ''

# Funções


def getvalor(event):
    global valores

    valores = valores + str(event)

    valor_texto.set(valores)


def calcular():
    global valores
    resultado = eval(valores)
    valor_texto.set(str(resultado))
    valores = str("")


def clean():
    valores = ""
    valor_texto.set("")


# criando label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=22, height=4,
                  padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor2)
app_label.place(x=0, y=0)


# criando botões
b1 = Button(frame_corpo, command=clean, text="C", width=18, height=3,
            bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(frame_corpo, command=lambda: getvalor('%'), text='%', width=7,
            height=3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=160, y=0)
b3 = Button(frame_corpo, command=lambda: getvalor('/'), text="÷", width=7, height=3,
            bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=240, y=0)
b4 = Button(frame_corpo, command=lambda: getvalor('*'), text='x', width=7, height=3,
            bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=240, y=71)
b5 = Button(frame_corpo, command=lambda: getvalor('-'), text="-", width=7, height=3,
            bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=240, y=142)
b6 = Button(frame_corpo, command=lambda: getvalor('+'), text="+", width=7, height=3,
            bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=240, y=213)
b7 = Button(frame_corpo, command=lambda: getvalor('7'), text="7", width=7,
            height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=0, y=71)
b8 = Button(frame_corpo, command=lambda: getvalor('8'), text="8", width=7,
            height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=80, y=71)
b9 = Button(frame_corpo, command=lambda: getvalor('9'), text="9", width=7,
            height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=160, y=71)
b10 = Button(frame_corpo, command=lambda: getvalor('4'), text="4", width=7,
             height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=0, y=142)
b11 = Button(frame_corpo, command=lambda: getvalor('5'), text="5", width=7,
             height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=80, y=142)
b12 = Button(frame_corpo, command=lambda: getvalor('6'), text="6", width=7,
             height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=160, y=142)
b13 = Button(frame_corpo, command=lambda: getvalor('1'), text="1", width=7,
             height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=0, y=213)
b14 = Button(frame_corpo, command=lambda: getvalor('2'), text="2", width=7,
             height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=80, y=213)
b15 = Button(frame_corpo, command=lambda: getvalor('3'), text="3", width=7,
             height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=160, y=213)
b16 = Button(frame_corpo, command=lambda: getvalor('0'), text="0", width=15,
             height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=284)
b17 = Button(frame_corpo, command=lambda: getvalor('.'), text=".", width=7,
             height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=160, y=284)
b18 = Button(frame_corpo, command=calcular, text="=", width=7, height=3,
             bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x=240, y=284)


janela.mainloop()
