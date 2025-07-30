import  numpy  as np

class Probability:
    def set_exp_pr(self, pop, pressure):
        # Assigns selection probabilities using exponential fitness scaling with selection pressure
        evaluations = np.array([p['evaluation'] for p in pop])
        weights     = np.exp(-pressure * evaluations)
        total       = np.sum(weights)
        for i, p in enumerate(pop):
            p['pr'] = weights[i] / (total + 1)
        return pop