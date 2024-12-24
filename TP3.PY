#exercice 1
from abc import ABC, abstractmethod
import math

class Form(ABC):
    @abstractmethod
    def calculer_surface(self):
        pass

class Rectangle(Form):
    def __init__(self, l, L):
        self.L = L
        self.l = l 
    def calculer_surface(self):
        return self.L*self.l 

class Cercle(Form):
    def __init__(self, rayon):
        self.rayon = rayon
    def calculer_surface(self):
        return math.pi*(self.rayon**2)
r1 = Rectangle(4,5)
c1 = Cercle(6)
print(r1.calculer_surface())
print(c1.calculer_surface())

#exercice2
class Personne:
    def __init__(self,nom,prenom,age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
    @property
    def nom(self):
        return self.__nom
    
    @property
    def prenom(self):
        return self.__prenom
    
    @property
    def age(self):
        return self.__age
    

    @age.setter
    def age(self,age):
        if age > 0:
            self.__age = age
        else: 
            print("Erreur")
        

p1 = Personne("LAMAHAD","Maryam",20)
print(p1.nom,p1.prenom,p1.age)

#exercice3
def afficher_surface(formes):
    for forme in formes:
        print(f"Surface : {forme.calculer_surface()}")

cercle = Cercle(5)
rectangle = Rectangle(4, 6)

formes = [cercle, rectangle]
afficher_surface(formes)

#exercice4
class Produit:
    def __init__(self,nom,prix):
        self.__nom = nom
        self.__prix = prix
    
    @property
    def nom(self):
        return self.nom 
    
    @property
    def prix(self):
        return self.prix
    
    @nom.setter
    def nom(self,nom):
        self.nom = nom

    @prix.setter
    def prix(self,prix):
        self.prix = prix
    
    def calculer_remise(self, remise,s):
            if self.__prix > s:
                return self.__prix *(1-remise)
            else :
                print("aucun remise ici: le prix doit être supérieur ou égal à ",s)
        

p1 = Produit("tab", 1600)

print(p1.calculer_remise(0.1,1500))

#exercice5
class Employe:
    def __init__(self, nom ,prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
    def __str__(self):
        return f"{self.nom} {self.prenom} :: Salaire: {self.salaire}"
    

class Menage(Employe):
    def __init__(self,nom, prenom, salaire):
        super().__init__(nom,prenom,salaire)
        self.employees = []
    def ajoute_employe(self,employe):
        return self.employees.append(employe)
    def affichage(self):
        if not self.employees:
            print("aucun employe")
        else:
            for employe in self.employees:
                print("+",employe)

emp1 = Employe("LAMAHAD","Maryam", 16000)
emp2 = Employe("A","C",15000)
mng = Menage("y","w",20000)
mng.ajoute_employe(emp1)
mng.ajoute_employe(emp2)
mng.affichage()


#exercice6
class Produit:
    def __init__(self, nom, prix):
        self._nom = nom
        self._prix = prix

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, value):
        if value >= 0:  
            self._prix = value
        else:
            raise ValueError("Le prix doit être positif.")


class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit
        self.quantite = quantite

    def calculer_total(self):
        return self.produit.prix * self.quantite


class Panier:
    def __init__(self):
        self.commandes = []

    def ajouter_commande(self, commande):
        self.commandes.append(commande)

    def calculer_total_panier(self):
        return sum(commande.calculer_total() for commande in self.commandes)

produit1 = Produit("Laptop", 1500)
produit2 = Produit("Souris", 50)

commande1 = Commande(produit1, 2)  
commande2 = Commande(produit2, 3) 

panier = Panier()
panier.ajouter_commande(commande1)
panier.ajouter_commande(commande2)

print(f"Total du panier : {panier.calculer_total_panier()} €")

#exercice7
from abc import ABC, abstractmethod

class Vehicule(ABC):
    @abstractmethod
    def deplacer(self):
        pass

class Voiture(Vehicule):
    def deplacer(self):
        return "La voiture roule ."

class Bicyclette(Vehicule):
    def deplacer(self):
        return "La bicyclette ."

voiture = Voiture()
bicyclette = Bicyclette()

print(voiture.deplacer())
print(bicyclette.deplacer())