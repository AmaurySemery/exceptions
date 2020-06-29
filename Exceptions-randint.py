from random import randint

nbr=-1
# nombre éléments
while nbr<0 or nbr>100:
    try:
        nbr=int(input("Saisir un nombre : "))
        print("Le nombre est bel et bien compris entre 0 et 100")
    except Exception as err:
        print("Erreur" + str(err))
        nbr=-1

tablo=[]

for i in range(0,nbr):
    tablo.append(randint(0,10))
    
print(tablo)