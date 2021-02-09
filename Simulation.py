from Population import Population


class Simulation:

    def __init__(self, phrase_a_trouver, taille_pop, pourcentage_selects, pourcentage_mut):
        self._phrase_a_trouver = phrase_a_trouver
        self._taille_population = taille_pop
        self._pourcentage_selections = pourcentage_selects
        self._pourcentage_mutations = pourcentage_mut

        pop = Population(self._taille_population, self._phrase_a_trouver)
        phrase_generee = False
        generation = 0
        while not(phrase_generee):
            pop.selection_pop(self._pourcentage_selections)
            print("Generation n°" + str(generation) + " - Le meilleur enfant génère la phrase:\n")
            if pop.get_selection():
                print("le mot : "+pop.get_selection()[0].get_phrase() +" Fitness :" + str(pop.get_selection()[0].get_fitness()))
                print("le mot : "+pop.get_selection()[1].get_phrase() +" Fitness :" + str(pop.get_selection()[1].get_fitness()))
                print("le mot : "+pop.get_selection()[2].get_phrase() +" Fitness :" + str(pop.get_selection()[2].get_fitness()))
                print("le mot : "+pop.get_selection()[3].get_phrase() +" Fitness :" + str(pop.get_selection()[3].get_fitness()))

            pop.crossover_pop2()

            pop.mutation_pop(self._pourcentage_mutations)
            if pop.get_individus()[0].get_fitness() == 1:
                phrase_generee = True

            generation += 1
            print("--------------------------")


        print("La phrase " + "'" + phrase_a_trouver + "' a été trouvée en " + str(generation) + " générations.")
