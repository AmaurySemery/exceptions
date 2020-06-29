# year <- saisir une année
# input ...
b_bonrep = False

while b_bonrep == False:
    s_year = input("Date ? >")
    # year est un string / chaîne de caractères
    # on test si year vaut 2000
    # '2000' =/= 2000
    if s_year == "2000":
        print("Bien joué !")
    try:
        i_yearnew=int(year)+10
        print(yearnew)
        b_bonrep= True
    except ZeroDivisionError:
        print("Division par 0 !")
    except Exception as error:
        print( error)
print("Fini !")

# refera le programme tant que ça plantera