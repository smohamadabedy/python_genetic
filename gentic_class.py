from kit.dependency_file import *
from kit.probability import *
from kit.sorting import *
from kit.selection import *
from kit.info_popup import *
from gentic_function import *

        
class population (info_popup,sorting,probability,selection):

    def __init__(self,space,settings,function):
        pop_dim = settings["total_population"]
        child_p = settings["child_percent"]
        mut_p = settings["muation_percent"]
        self.slct_method = settings["muation_percent"]
        self.sort_method = settings["sorting"]
        self.prob_method = settings["probability"]
        self.prob_press = settings["probability_pressure"]
        self.pspace = space
        self.gval_function = function
        self.pshape = self.pspace.shape
        self.ndim = self.pshape[0]
        self.pdim = pop_dim
        self.cdim = 2*math.ceil(child_p*self.pdim/2)
        self.mdim = math.ceil(mut_p*self.pdim)
        self.parents = np.array([])
        self.child = np.array([])
        self.mutation = np.array([])
        self.pop = (self.init_pop())
        self.generation = np.array([])
        
    def generate_inital_value(self):
        vallist = []
        for x in range(0,self.ndim):
            vallist.append(random.uniform(self.pspace[x][0],self.pspace[x][1]))
        return vallist
    
    def create_init_particle(self):
            values = self.generate_inital_value()
            f_eval = self.gval_function(values)
            newparticle = {
                "pr" : 1,
                "age" : 0,
                "value" : values,
                "evaluation" : f_eval, 
                }
            return newparticle

    def init_pop(self):
        cart = []
        for x in range(0,self.pdim):
            cart.append(self.create_init_particle())
        return np.array(cart)

    def pop_aged(self,val = 1):
        for x in self.pop:
            (x['age']) += val
        return self

    def generate_crossovers(self):
          return [random.uniform(-1.5,1.5) for x in range(0,self.ndim)]

    def create_child(self,p1,p2,alpha):
        values1 = []
        values2 = []
        for x in range(0,self.ndim):
            val1 = ((p1["value"][x])*alpha[x]) + ((p2["value"][x])*(1-alpha[x]))
            val2 = ((p1["value"][x])*(1-alpha[x])) + ((p2["value"][x])*(alpha[x]))
            values1.append(val1)
            values2.append(val2)
            
        f_eval1 = self.gval_function(values1)
        f_eval2 = self.gval_function(values2)

        
        newparticle1 = {
                "pr" : 1,
                "age" : 0,
                "value" : values1,
                "evaluation" : f_eval1, 
                }
        newparticle2 = {
                "pr" : 1,
                "age" : 0,
                "value" : values2,
                "evaluation" : f_eval2, 
                }
        return [newparticle1 , newparticle2]
        
    ###add your own sorting method within elif 
    def sort_pop (self,pop):
       if (self.sort_method == 'buble'):
           self.buble_sort(self.pop)
           return self
       elif():
            return self
       else:
           self.buble_sort(self.pop)
           return self
        
    ### add your own probabilty setting within elif
    def set_pr(self,pop):
        pressure = self.prob_press
        if(self.prob_method == 'exp'):
             self.set_exp_pr(pop,pressure)
             return self
        elif():
            return self
        else:
             self.set_exp_pr(pop,pressure)
             return self

    ### add your own selection within elif
    def select_parents(self):
        if(self.slct_method == 'simple'):
            self.parents = self.simple_select()
            return self
        elif():
            return self
        else:
            self.parents = self.simple_select()
            return self

            
    ### fisrt step in optimization _ sorting and setting priority 
    def step_one(self):
        self.generation = np.array([])
        self.parents = np.array([])
        self.child = np.array([])
        self.mutation = np.array([])
        self.set_pr(self.pop).sort_pop(self.pop)
        return self


    def breeding(self):
        parenting = self.parents

        while(parenting.shape[0] > 0):
            first = random.randint(0,parenting.shape[0])
            parent_first = parenting[first]
            parenting = np.delete(parenting,first)
            second = random.randint(0,parenting.shape[0])
            parent_second = parenting[second]
            parenting = np.delete(parenting,second)
            alpha = (self.generate_crossovers())
            new_child = self.create_child(parent_first,parent_second,alpha)
            self.child = np.append(self.child,new_child)
        return self
    
    def pop_done(self):
        for x in self.pop:
            self.generation = np.append(self.generation,x)
        for y in self.child:
            self.generation = np.append(self.generation,y)
        for z in self.mutation:
            self.generation = np.append(self.generation,z)

        self.set_pr(self.generation).sort_pop(self.generation)

        self.pop = np.array([])
        cart = []
        for iteration in range(0,self.pdim):
           cart.append(self.generation[iteration])
        self.pop = np.array(cart)    
        return self
    
    def mutatating(self):
        cart =[]
        for x in range(0,self.mdim):
            cart.append(self.create_init_particle())
        self.mutation = np.array(cart)
        return self




