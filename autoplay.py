import sys, os
import subprocess

dir_path = os.path.dirname(os.path.realpath(__file__))
dirp = str(dir_path)+"/"
def gen():
   f= open(dirp+"links.txt","r")
   g= open(dirp+"newlinks.txt","r")
   urls = f.readlines() + g.readlines()
   urls = [i[:-1] for i in urls]
   print(urls)
   f.close()
   out=[]
   for i in urls:
      out.append(genOut(str(i)))


   output(out)
   print("gen done!")

def output(out):
	
   o = open(dirp+"out.txt","w")
   for i in out:
      s=str(i)
      print(s)
      o.write(s)
   o.close()
   
def play(k=-1):
   f=open(dirp+"out.txt","r")
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
	
   k = int(k)
   if k==-1:
      print(urls)
      for u in urls:
         os.system('omxplayer -o hdmi '+p+ str(u)+p )
   elif (k<len(urls)):
      print(urls[k])
      os.system('omxplayer -o hdmi '+p+ urls[k]+p )
   else:
      print("nope")
	
   print("play done!")
   return urls

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
   f= open(dirp+"newlinks.txt","a")
   f.write(str(link)+"\n")
   f.close()
   out=[]
   out.append(genOut(link))
	
   o = open(dirp+"out.txt","a")
   for i in out:
      s=str(i)
      o.write(s)
   o.close()

   print("add done!")

def genplay():
    gen()
    play()
