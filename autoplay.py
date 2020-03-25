import sys, os
import subprocess

def gen():
   f= open("links.txt","r")
   urls = f.readlines()
   urls = [i[:-1] for i in urls]
   print(urls)
   f.close()
   out=[]
   for i in urls:
      out.append(genOut(i))

	
   print(out)
   output(out)
   print("gen done!")

def output(out):
   s="b'"
   out = out.split(s)
   out =[u[:-3] for u in out]
	
   o = open("out.txt","w")
   [o.write(str(i)) for i in out if str(i) != '']
   o.close()

def play(k=-1):
   f=open("out.txt","r")
   urls=f.read()
   print(urls)
   print("-----------")
   p="'"
   print(urls)
   f.close()

   if k==-1:
      for u in urls:
         os.system('omxplayer -o hdmi '+p+ str(u)+p )
   elif (k<len(urls)):
      os.system('omxplayer -o hdmi '+p+ urls[k]+p )
   else:
      print("nope")
   print("play done!")


def genOut(link):

      yta = ['youtube-dl', '-g','-f','best',link, '--restrict-filenames']
      yt = subprocess.Popen(yta,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
      (res,err) = yt.communicate()
      if res and not err:
         print("no error")
         return res
      else:
         print("err")
         return res
		 
def addlink(link):
   f= open("links.txt","a")
   f.write(str(link))

   out=[]
   out.append(genOut(link))
   output(out)

   print("add done!")

def genplay():
    gen()
    play()
