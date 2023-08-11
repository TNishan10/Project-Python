file = open("laptop.txt","r")
laptop_id=1
mydict={}
for line in file:
     line = line.replace("\n","")
     mydict.update({laptop_id: line.split(",")})
     laptop_id+=1