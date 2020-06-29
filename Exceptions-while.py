# year <- saisir une année
# input ...
bonrep = False

while bonrep == False:
    year = input("Date ? >")
    # year est un string / chaîne de caractères
    # on test si year vaut 2000
    # '2000' =/= 2000
    if year == "2000":
        print("Bien joué !")
    try:
        yearnew=int(year)+10
        print(yearnew)
        bonrep= True
    except ZeroDivisionError:
        print("Division par 0 !")
    except Exception as error:
        print( error)
print("Fini !")

# refera le programme tant que ça plantera