import random as rd
options = ["Tura","Yazı"]
sayac=0
a = int(input("Kaç defa atılsın>> "))
while sayac<a:
    
    durum=rd.randint(0,1)
    print(options[durum]+'\n')
    sayac+=1