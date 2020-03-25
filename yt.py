import sys, os
import subprocess

gen():
   f= open("links.txt","r")
   urls = f.readlines()
   urls = [i[:-1] for i in urls]
   print(urls)
   f.close()
   out=[]
   for i in urls:
      yta = ['youtube-dl', '-g',i, '--restrict-filenames']
      yt = subprocess.Popen(yta,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
      (res,err) = yt.communicate()
      
      if res and not err:
         out.append(res)
      
   o = open("out.txt","w")
   o = [i.read() for i in out]
   o.close()

play():
   f=open("out.txt","r")
   f=f.read()
   urls = f.split(,)
   print(urls)
   f.close()
   os.system('omxplayer -o hdmi '+"'"+str(urls[1])+"'")
   


