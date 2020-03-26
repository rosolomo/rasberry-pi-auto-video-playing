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
      out.append(genOut(str(i)))


   output(out)
   print("gen done!")

def output(out):
	
   o = open("out.txt","w")
   for i in out:
      s=str(i)
      print(s)
      o.write(s)
   o.close()
   
def play(k=-1):
   f=open("out.txt","r")
   urls=f.read()
   #print(urls)
   print("-----------")
   urls=urls.split("\\n'b'")
   #print(urls)
   urls[0]=urls[0][2:]
   urls[-1]=urls[-1][:-3]
   #print(urls)
   f.close()
   p="'"
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
   f.close()
   out=[]
   out.append(genOut(link))
	
   o = open("out.txt","a")
   for i in out:
      s=str(i)
      o.append(s)
   o.close()

   print("add done!")

def genplay():
    gen()
    play()
