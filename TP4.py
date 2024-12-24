
class Vehicule:
    def __init__(self, marque, modele, annee): 
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_info(self):
        return f"Marque: {self.marque}, Modèle: {self.modele}, Année: {self.annee}"


class Moteur:
    def __init__(self, puissance, type_moteur): 
        self.puissance = puissance
        self.type_moteur = type_moteur

    def afficher_moteur(self):
        return f"Puissance: {self.puissance} chevaux, Type de moteur: {self.type_moteur}"


class Voiture(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, nombre_de_places):
        Vehicule.__init__(self, marque, modele, annee)  
        Moteur.__init__(self, puissance, type_moteur)  
        self.nombre_de_places = nombre_de_places

    def afficher_info(self):
        info_vehicule = Vehicule.afficher_info(self)
        info_moteur = Moteur.afficher_moteur(self)
        return f"{info_vehicule}, Nombre de places: {self.nombre_de_places}\n{info_moteur}"


class Moto(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, type_moto):
        Vehicule.__init__(self, marque, modele, annee) 
        Moteur.__init__(self, puissance, type_moteur)  
        self.type_moto = type_moto

    def afficher_info(self):
        info_vehicule = Vehicule.afficher_info(self)
        info_moteur = Moteur.afficher_moteur(self)
        return f"{info_vehicule}, Type de moto: {self.type_moto}\n{info_moteur}"


voiture = Voiture("Dacia", "Sandero", 2020, 120, "Essence", 5)

moto = Moto("Ya", "MT7", 2022, 75, "Essence", "Sport")


print("Informations sur la voiture:")
print(voiture.afficher_info())
print("\nInformations sur la moto:")
print(moto.afficher_info())
