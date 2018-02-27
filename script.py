#!/usr/bin/python3.1

#print ("Salut les gens")

'''
a=10
b=5
print (a+b)
'''


'''
age ="je suis vieux"

print (age)

age = "je suis jeune"

print (age)
'''


'''
text = "je suis du texte"

print ( text * 3 )
'''


''''
txt = "Hello Wolrd!!!!"

print (len(txt))
print (txt[1])
print (txt[0:5])
'''


'''
print ("bonjour je m'appelle %s" %("Tchalla"))
'''

#Echappement

'''text = "je suis du \"texte\""
#Ou : text = 'je suis du "texte"'
print (text)'''



#Liste

'''
liste=[]

print (type(liste))

liste=[1,2,3]

print (liste)
'''


'''
maListe = []

maListe.append(1)

print (maListe)

maListe.append("salut")

print (maListe)
'''


'''
maListe = ["1er", "deuxieme","troisieme"]
#supprimer avec l'index
del maListe[1]
print(maListe)

#supprimer avec la valeur
maListe.remove("troisieme")
print(maListe)'''

'''

#changer index
maListe.reverse

#compter

print(maListe.count("1er"))

#trouver index d'une valeur
print(maListe.index("1er"))

'''



'''
#BAAAD
maListe =["1er","deuxieme","troisieme"]

secondList = maListe

maListe[0] = "toto"

#Goood

print(secondList)maListe =["1er","deuxieme","troisieme"]

secondList = maListe[:]

maListe[0] = "toto"

print(secondList)
'''



'''
#Verifications
maListe = ["1er","deuxieme","troisieme"]

print ("1er" in maListe)

print ("toto" in maListe)'''

'''maListe = range (15)
liste = list(range(10))
liste.extend(maListe)
print(liste)
'''


'''
#Tuple : liste qui ne peut plus etre modifie

monTuple = ()
print (type (monTuple))
monTuple=("toto",)
print (type(monTuple))
monTuple[0]="error"
'''

'''
#Dictionnaire liste avec des clés numérique
monDico={}
monDico["name"]="steph"
monDico["height"]="1m90"

print(monDico)
'''


#Functions
'''
def ma_function():
	print ("Salut les gens")

ma_function()

def ma_function(param):
	print(param)

ma_function("hey")

def somme(a,b):
	return a+b

somme = somme (1,2)

print (somme)
'''
'''
def splat_function(*params):
	print(params[0])
	print(params[1])
	print(params[2])

splat_function(1,2,"Salut")
'''
#Porté des variables
'''
a = "salut"
c = 5
def test ():
	b = test
	print (c)

test()
print (a)
print(b)
'''

'''
#Recupere une entree dans le terminal / faire un get.type pourt etre sur de la valeur 
valeur=input("Enter your value")

#Retourne une valeur d'une liste aleatoirement
random.choice([1,2,3,4,5])
'''
'''
def exo01():
	i = 0
	while i < 500:
		print
'''


