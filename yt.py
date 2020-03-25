import sys, os
import subprocess

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




