import sys, os
import subprocess

f= open("links.txt",r)
urls = f.readline()
print(urls)

quit()
url='https://www.youtube.com/watch?v=vw61gCe2oqI'
yta = ['youtube-dl', '-g',url, '--restrict-filenames']
yt = subprocess.Popen(yta,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
(res,err) = yt.communicate()
if res and not err:
   print(res)

 os.system('omxplayer -o hdmi '+str(res))
