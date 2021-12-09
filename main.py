from tkinter import * 
from tkinter import ttk
from tkinter import font 

#importando Pillow 

from PIL import Image, ImageTk


#--------------------- cores  usadas ---------------------
cor0 = "#444466"  # preta
cor1 = "#feffff"  # branca
cor2 = "#6f9fbd"  # azul
cor3 = "#38576b"  # valor
cor4 = "#403d3d"   # letra

fundo = "#3b3b3b"

#--------------------- definindo a janela ---------------------
janela = Tk()
janela.title()
janela.geometry('500x300')
janela.configure(bg=fundo)

#--------------------- criando uma linha horizontal ---------------------
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=250)


#--------------------- dividindo a janela em 2 ---------------------

frame_cima = Frame(janela, width=500, height=110, bg=fundo, pady=5, padx=0)
frame_cima.grid(row=1, column=0,)

frame_baixo = Frame(janela, width=500, height=300, bg=cor1, pady=12, padx=0)
frame_baixo.grid(row=2, column=0, sticky=NW)

#--------------------- configurando o frame de cima ---------------------

logo = Image.open('images/icone_youtube.png')
logo = logo.resize((50,50), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)

l_logo = Label(frame_cima, image=logo, compound=LEFT, bg=fundo, font=('Ivy 10 bold'), anchor='nw')
l_logo.place(x=5, y=5)

l_name = Label(frame_cima, text="Youtube Download App", width=32, fg=cor1, compound=LEFT,bg=fundo, font=('Ivy 15 bold'), anchor='nw')
l_name.place(x=65, y=15)

l_url = Label(frame_cima, text="Entre o link", width=32, fg=cor1, compound=LEFT,bg=fundo, font=('Ivy 10 bold'), anchor='nw')
l_url.place(x=10, y=80 )
e_url = Entry(frame_cima, width=50, justify='left', relief=SOLID)
e_url.place(x=100, y=80 )

b_pesquisa = Button(frame_cima, text="Pesquisar", width=10, fg=cor1, compound=LEFT,bg=cor2, font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE)
b_pesquisa.place(x=404, y=81)



janela.mainloop()
