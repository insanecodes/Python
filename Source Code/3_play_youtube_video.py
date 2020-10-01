import vlc 
import pafy

url = input("Paste your YouTube URL here:>> ")

video = pafy.new(url)
best = video.getbest()

media = vlc.MediaPlayer(best.url)
media.play()