from autoplay import play

f=open("links.txt","r")

g = open("newlinks.txt","r")
numLinks = len(f.readlines()) + len(g.readlines())
                                    
print("num vids: ",numLinks)
n = input("how many vids do u want to play: ")
l = input("how many times do you want to loop: ")

vids=[]
print("enter vid numbers")
for i in range(int(n)):
  in = input("vid"+str(i)+": ")
  vids.append(i)

for i in range(int(l)):
  [play(v) for v in vids]
