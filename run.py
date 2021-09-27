from gentic_class import *


space = np.array([[-20,20],[-3,3]])
settings = {
    "total_population" : 50,
    "child_percent" : .6,
    "muation_percent" : .1,
    "selection" : "simple" ,
    "sorting" : "buble" ,
    "probability" : "exp",
    "probability_pressure" : 1,
    }

pop =  population(space,settings,function = gv_function)
pop.init_info()
pop.step_one().pop_aged(1).select_parents().breeding().mutatating().pop_done()
pop.step_one().pop_aged(1).select_parents().breeding().mutatating().pop_done()
pop.step_one().pop_aged(1).select_parents().breeding().mutatating().pop_done().excel_export()
pop.step_one().pop_aged(1).select_parents().breeding().mutatating().pop_done().excel_export()
pop.show_pop()

