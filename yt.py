import sys, os
import subprocess

gen():
   f= open("links.txt","r")
   urls = f.readlines()
   urls = [i[:-1] for i in urls]
   print(urls)
   
   out=[]
   for i in urls:
      yta = ['youtube-dl', '-g',i, '--restrict-filenames']
      yt = subprocess.Popen(yta,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
      (res,err) = yt.communicate()
      
      if res and not err:
         out.append(res)
      
   o = ("out.txt","w")

play():
   f=open("out.txt","r")
   f=f.read()
   urls = f.split(,)
   print(urls)
   s='cat'
   print("'"+s+"'")
   os.system('omxplayer -o hdmi '+str(urls[1]))
   


