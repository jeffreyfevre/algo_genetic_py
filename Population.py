import Individu
import random


class Population:
    """Une population est une liste d'individu
    Elle comprends les fonctions de crossover, de mutation"""

    # Attributes
    _individus = []
    _selection_pop = []

    # Constructor
    def __init__(self, nombre_individus, mot_a_trouver):
        self._phrase = mot_a_trouver
        self._taille_pop = nombre_individus
        for _ in range(self._taille_pop):
            individu = Individu.Individu()
            individu.generate_phrase(len(mot_a_trouver))
            individu.calcul_fitness(mot_a_trouver)
            self._individus.append(individu)

    # Methods
    def selection_pop(self, pourcentage_entre):
        # Fonction lambda qui trie les objets "Individu" par fitness en ordre décroissant
        self._individus.sort(key=lambda x: x._fitness, reverse=True)
        # Vérification valeurs de pourcentage_entre
        if isinstance(int, pourcentage_entre) and 0 < pourcentage_entre < 100:
            pourcentage_pop = (len(self._individus) // 100) * pourcentage_entre
            self._selection_pop = self._individus[:pourcentage_pop]
        else:
            print("La valeur de pourcentage n'est pas correcte.")

    def crossover_pop1(self):
        new_pop = []
        for _ in range(self._taille_pop):
            # Génération de deux parents choisis dans la population sélectionnée
            parent_1, parent_2 = random.sample(self._selection_pop, 2)

            # Aléatoire sur taille du parent moins 2
            gene_parent = random.randrange(1, len(parent_1) - 1)
            phrase_enfant = parent_1[0:gene_parent] + parent_2[gene_parent:]

            # Création d'un enfant de deux individus auquel on attribue la phrase généré
            enfant_individu = Individu.Individu()
            enfant_individu.set_phrase(phrase_enfant)
            enfant_individu.calcul_fitness(self._phrase)

            # Ajout de cet enfant dans la nouvelle population
            new_pop.append(enfant_individu)

        self._individus = new_pop
        return self._individus

    def crossover_pop2(self):
        mot_bebe = ""
        cross = []
        for _ in range(len(self._individus)):
            p1, p2 = random.sample(self._selection_pop, 2)
            for i in range(len(p1)):
                if random.randrange(0, 2) == 1:
                    mot_bebe += p1[i]
                else:
                    mot_bebe += p2[i]
            ind = Individu.Individu()
            ind.set_phrase(mot_bebe)
            ind.calcul_fitness(self._phrase)
            cross.append(ind)
            mot_bebe = ""
        self._individus = cross
        return self._individus

    def mutation_pop(self, pourcentage):
        population_mutante = []
        # String faisant office de liste de caractères
        gen_characters = 'abcdefghijklmnopqrsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.0123456789 '

        # On parcourt la liste d'individus
        for individu in self._individus:
            nombre_aleatoire = random.randrange(0, pourcentage + 1)
            if pourcentage < nombre_aleatoire:
                phrase_individu = individu.get_phrase()

                # Index de la lettre à muter
                index_mutant = random.randrange(len(individu.get_phrase()))

                # Transformation en liste
                liste_phrase_individu = list(phrase_individu)

                # Modification du caractère à l'index choisi précédemment
                liste_phrase_individu[index_mutant] = random.choice(gen_characters)
                mot_mutant = ''.join(liste_phrase_individu)

                # Changement de la phrase et nouveau calcul de l'individu
                individu.set_phrase(mot_mutant)
                individu.calcul_fitness(self._phrase)
                population_mutante.append(individu)

        self._individus = population_mutante
        return self.get_individus()

    # Accessors / Mutators
    def get_individus(self):
        return self._individus

    def set_individus(self, liste_individus):
        self._individus = liste_individus

    def get_selection(self):
        return self._selection_pop

    def get_taille_pop(self):
        return self._taille_pop

    def set_taille_pop(self, taille_pop):
        self._taille_pop = taille_pop
