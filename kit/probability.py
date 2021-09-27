from kit.dependency_file import *

class probability:
        
    def set_exp_pr(self,pop,pressure):
        self.pop  = pop;
        sigma = 0;
        for x in (pop):
            sigma += (math.exp(-pressure * x['evaluation']));
        for x in pop:
            x['pr'] = (math.exp(-pressure * x['evaluation'])) / sigma;
        return pop;
