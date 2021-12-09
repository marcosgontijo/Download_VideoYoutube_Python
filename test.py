from pytube import YouTube

import datetime
import calendar


YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
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


print(titulo, "\n" , views,"\n" , duracao,"\n" , info,"\n" , foto)