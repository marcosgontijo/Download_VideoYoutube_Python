from tkinter import * 
from tkinter import ttk
from tkinter import font 

#importando Pillow 

from PIL import Image, ImageTk

from pytube import YouTube

import datetime
import calendar



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

frame_baixo = Frame(janela, width=500, height=300, bg=fundo, pady=12, padx=0)
frame_baixo.grid(row=2, column=0, sticky=NW)

#--------------------- configurando o frame de cima ---------------------

logo = Image.open('images/icone_youtube.png')
logo = logo.resize((50,50), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)

l_logo = Label(frame_cima, image=logo, compound=LEFT, bg=fundo, font=('Ivy 10 bold'), anchor='nw')
l_logo.place(x=5, y=5)

l_name = Label(frame_cima, text="Youtube Download App", width=32, fg=cor1, compound=LEFT,bg=fundo, font=('Ivy 15 bold'), anchor='nw')
l_name.place(x=65, y=15)

#funcao pesquisar, vai receber a url e realizar a manipulação
def pesquisar():
    yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')

        # titulo do video 
    titulo = yt.title

    #visualizações video
    views = yt.views

    #duração do video
    duracao = str(datetime.timedelta(seconds=yt.length))

    #descricao do video
    info = yt.description

    #descricao do video
    foto = yt.thumbnail_url




l_url = Label(frame_cima, text="Entre o link", width=32, fg=cor1, compound=LEFT,bg=fundo, font=('Ivy 10 bold'), anchor='nw')
l_url.place(x=10, y=80 )
e_url = Entry(frame_cima, width=50, justify='left', relief=SOLID)
e_url.place(x=100, y=80 )

b_pesquisa = Button(frame_cima, text="Pesquisar", width=10, fg=cor1, compound=LEFT,bg=cor2, font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE)
b_pesquisa.place(x=404, y=81)

# operacoes

l_imagem = Label(frame_baixo, image=logo, compound=LEFT, bg=fundo, font=('Ivy 10 bold'), anchor='nw')
l_imagem.place(x=10, y=10)

l_titulo = Label(frame_baixo, text="Titulo do video", height=2, wraplength=225, fg=cor1, compound=LEFT, bg=fundo, font=('Ivy 10 bold'), anchor='nw')
l_titulo.place(x=250, y=15)

l_views = Label(frame_baixo, text="10,100,10", width=32, fg=cor1, bg=fundo, font=('Ivy 8 bold'), anchor='nw')
l_views.place(x=250, y=60)

l_time = Label(frame_baixo, text="00:02:50", width=32, fg=cor1, bg=fundo, font=('Ivy 8 bold'), anchor='nw')
l_time.place(x=250, y=85)


#botao download
down = Image.open('images/download.png')
down = down.resize((29,29), Image.ANTIALIAS)
down = ImageTk.PhotoImage(down)

b_down = Button(frame_baixo, image=down, compound=LEFT, bg=fundo, font=('Ivy 10 bold'), overrelief=RIDGE)
b_down.place(x=444, y=85)







janela.mainloop()
