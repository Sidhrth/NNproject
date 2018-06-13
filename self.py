import numpy as np

#inputs
X = np.array(([100, 20, 3000], [400, 5, 100], [240, 10, 1000]), dtype=float)
y = np.array(([300], [900], [500]), dtype=float)


X = X/np.amax(X, axis=0)
y = y/1000 

class NeuralNetwork:
    def __init__(self):
        self.inputnodes = 3
        self.outputnodes = 1
        self.hiddennodes = 3
    
    #weights
        self.W1 = np.random.randn(self.inputnodes, self.hiddennodes)
        self.W2 = np.random.randn(self.hiddennodes, self.outputnodes)

nn = NeuralNetwork()
print "w1 =" + str(nn.W1) + "\n W2 = " + str(nn.W2)