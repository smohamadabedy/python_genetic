# python_genetic
python_genetic multi-dimensional optimization solver

first add your own function in gv_function file in main folder then edit run file :
  <pre>
  
  from gentic_class import *


# determine search space and optimization dimention
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

# step 1
pop.step_one().pop_aged(1).select_parents().breeding().mutatating().pop_done()
# step 2
pop.step_one().pop_aged(1).select_parents().breeding().mutatating().pop_done()
# step 3 - with excel export
pop.step_one().pop_aged(1).select_parents().breeding().mutatating().pop_done().excel_export()
# step 4 - with excel export
pop.step_one().pop_aged(1).select_parents().breeding().mutatating().pop_done().excel_export()

pop.show_pop()
  
  </pre>
  
