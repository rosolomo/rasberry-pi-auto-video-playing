import sys, os


f = open("links.txt", "r")
f=f.read()
links = [x for x in f]
url=os.system('youtube-dl -g '+ links[0])
os.system('omxplayer -o hdmi '+url)
