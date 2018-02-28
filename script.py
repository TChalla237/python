#!/usr/bin/python3.1
#!/usr/bin/env python
# coding: utf-8

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


#Modules et packages

'''
#func.py (nom du fichier)
def addition(a,b):
	return a+b

#script.py (nom du fichier)

from func import *
print(addition(5,10))

'''

# Modules : un fichier qui comprend plusieurs fonctions

# Package : Ensemble de module

#TRY
'''
a = 1 
b= 0
try: 
	a/b
	print("ok")
except:
	print("Error")

'''
#Programmation orientée Objets / Classes
'''
class Voiture:
	def __init__(self):
		self.nom="Ferrari"

ma_voiture = Voiture() #Instantiation : creation objet par une class
print(ma_voiture.nom)


#Fonction dans une classe n'est pas une fonction mais une METHODE
'''


#Encodage 
 #chaque debut de script : 
 #!/usr/bin/env python
 # coding: utf-8

#PIP (equivalent apt-get pour python)


#Socket 

#Point d'entrée sur un réseau
'''
import socket

ip = socket.gethostbyname(socket.gethostname()) #ip local de la machine

print(ip)
'''
'''
import os

subnet = "192.168.0."

for i in range(1,255):
	hostname = subnet + str(i)
	response = os.system("ping -n 1 " + hostname)
	if response == 0:
		print(hostname, 'is up!')

'''


#Machine learning !!

