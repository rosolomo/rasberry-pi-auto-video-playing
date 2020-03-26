from autoplay import play

f=open("links.txt","r")

g = open("newlinks.txt","r")
numLinks = len(f.readlines()) + len((g.readlines))
print("Num Vids")
n = input("how many vids do u want to play: ")
l = input("how many times do you want to loop: "

vids=[]
print("enter vid numbers")
for i in range(n):
  vids.append(input("vid ",i))

for i in range(l):
  [play(v) for v in vids]
