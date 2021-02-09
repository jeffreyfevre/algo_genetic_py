from Population import Population


class Simulation:
    _nombre_generations = 0


    def __init__(self, phrase_a_trouver, taille_pop, pourcentage_selects, pourcentage_mut):
        self._phrase_a_trouver = phrase_a_trouver
        self._taille_population = taille_pop
        self._pourcentage_selections = pourcentage_selects
        self._pourcentage_mutations = pourcentage_mut

        pop = Population(self._taille_population, self._phrase_a_trouver)
        phrase_generee = False
        generation = 0
        while(phrase_generee):
            pop.selection_pop(self._pourcentage_selections)
            print("Generation n°" + generation + " ")
            pop.crossover_pop1()
            pop.mutation_pop(self._pourcentage_mutations)
            for individu in pop.get_individus():
                if individu.get_phrase() == self._phrase_a_trouver:
                    phrase_generee = True
                else:

            gener
