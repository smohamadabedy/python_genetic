from kit.dependency_file import *

class sorting:

    def buble_sort(self,pop):
        length = pop.shape[0];
        while (1):
            c = 0
            for x in range(0,length-1):
                xx1 = pop[x];
                xx2 = pop[x+1];
                if(xx1["evaluation"] > xx2["evaluation"]):
                    pop[x] = xx2;
                    pop[x+1] = xx1;
                    c = c+1;
            if(c == 0):
                break;
        return (pop);
