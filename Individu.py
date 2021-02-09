import random

class Individu:
    """Individu contenant une phrase et un fitness généré à partir de celle-ci"""

    # Attributs
    _phrase = ""
    _fitness = 0

    # Constructor

    # Methods
    def generate_phrase(self, taille_phrase):
        gen_characters = 'abcdefghijklmnopqrsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.0123456789 '
        mot_genere = (''.join(random.choices(gen_characters, k=taille_phrase)))
        self.set_phrase(mot_genere)
        return self.get_phrase()


    def calcul_fitness(self, mot_a_trouver):
        i = 0
        compteur = 0
        for lettre in mot_a_trouver:
            if lettre == self._phrase[i]:
                compteur += 1
            i += 1
        self._fitness = compteur / len(mot_a_trouver)

    # Accessors Mutators
    def get_phrase(self):
        return self._phrase

    def set_phrase(self, phrase):
        self._phrase = phrase

    def get_fitness(self):
        return self._phrase

    def set_fitness(self, fitness):
        self._fitness = fitness
