from python_genetic import GA

# ---------------- Benchmark Functions ------------------
def sphere_3d(x):
    return sum(i ** 2 for i in x[:3])



# Define the configuration settings for the Genetic Algorithm
settings = {
             "space"                 : ([[-100, 100], [-100, 100], [-100, 100]]),            # Search space for each dimension
             "total_population"      : 50,                                                  # Number of individuals in the population
             "mutation_rate"         : 0.1,                                                  # Fraction of new individuals introduced through mutation
             "selection"             : "simple",                                             # Parent selection method (e.g., simple random)
             "selection_rate"        : 0.5,                                                  # Fraction of top individuals selected for mating
             "sorting"               : "bubble",                                             # Sorting method for ranking individuals
             "probability"           : "exp",                                                # Type of selection probability distribution
             "probability_pressure"  : 1,                                                    # Pressure factor for exponential probability distribution
            }

# Initialize the population with given settings and the target fitness function
pop = GA(settings, fitness=sphere_3d)

# Run the Genetic Algorithm for 50 iterations
for i in range(50):
    (   pop.mate()               # Select parents from the current population
            .breed()             # Generate offspring through recombination of parents
            .mutate()            # Introduce random individuals (mutation)
            .repopulate()        # Form the next generation by selecting the best individuals
            .log_iteration(i)    # Record statistics for the current generation
    )

# Save the history of optimization results to files (JSON and CSV)
pop.save_history()

# Plot the optimization history (e.g., best score over generations)
pop.plot()

