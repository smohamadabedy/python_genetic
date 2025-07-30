class Sorting:
    def bubble_sort(self, pop):
        # Sorts the population in ascending order based on 'evaluation' (fitness value) using bubble sort
        n = len(pop)
        while True:
            swapped = False
            for i in range(n - 1):
                if pop[i]['evaluation'] > pop[i + 1]['evaluation']:
                    pop[i], pop[i + 1] = pop[i + 1], pop[i]
                    swapped = True
            if not swapped:
                break
        return pop
