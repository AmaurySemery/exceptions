try:
    a = 14/0
    print(a)
except Exception as error:
    # ou : except ZeroDivisionError as error :
    #           print("Division par 0 !")
    print("Aïe :" + str(error))
    # ou : print(error)
print("fini !")

# on peut aussi faire comme ça :

try:
    a = 14/0
    print(a)
except ZeroDivisionError:
    print("Division par 0 !")
    
except Exception:
    print("j'ai planté !")

print("fini !")

# En l'occurrence, si l'erreur est une division par zéro, c'est la première commande except qui s'activera 
# Si c'est un autre type d'erreur, c'est la deuxième commande except qui s'activera
# https://docs.python.org/fr/3/tutorial/errors.html pour aller plus loin