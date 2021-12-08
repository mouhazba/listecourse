import json
import os
import logging

from constants import DATA_DIR
print(DATA_DIR)
os.path.join(DATA_DIR, "test.json ")

LOGGER = logging.getLogger()

class Liste(list):
    def __init__(self, nom):
        self.nom = nom.title()

    def ajout(self, element):
        #si element n'est pas de type string lever une exception
        if not isinstance(element, str):
            raise ValueError("Vous ne pouvez ajouter que des chaines")

        if element in self:
            LOGGER.error(f"{element} est dèja dans la liste")
            return False

        self.append(element)
        return True

    def enlever(self, el):
        if el in self:
            self.remove(el)
            return True
        return True

    def afficher(self):
        print(f"Ma liste de  {self.nom}")
        for el in self:
            print(f"- {el}")

    def sauvegarder(self):
        chemin = os.path.join(DATA_DIR, "test.json ")
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        with open(chemin , "w") as f:
            json.dump(self, f, indent=4)

        return False

if __name__ == "__main__":
    liste = Liste("Poulet")
    liste.ajout("categorie-1 4000f")
    liste.ajout("categorie-2 2800f")

    liste.sauvegarder()

