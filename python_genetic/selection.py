class Selection:
    # Simply select a portion of the sorted population for crossover based on the "selection_rate"
    def simple_select(self):
        return self.pop[:self.cdim]