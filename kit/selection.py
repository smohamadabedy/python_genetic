from kit.dependency_file import *

class selection:
    def simple_select(self):
        cart = np.array([]);
        for x in range(0,self.cdim):
            cart = np.append(cart,self.pop[x]);
        return cart;
