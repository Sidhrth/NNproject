import numpy as np

#example is housing prices
# X input variables - size, age, distance to market
X = np.array(([100, 20, 3000], [400, 5, 100], [240, 10, 1000]), dtype=float)
y = np.array(([300], [900], [500]), dtype=float)

# Feature scaling
X = X/np.amax(X, axis=0)
y = y/1000 



class Neural_Network(object):
  def __init__(self):

    self.inputnodes = 3
    self.outputnodes = 1
    self.hiddennodes1 = 3
    self.hiddennodes2 = 3

    #weights
    self.W1 = np.random.randn(self.inputnodes, self.hiddennodes1) 
    self.W2 = np.random.randn(self.hiddennodes1, self.hiddennodes2)
    self.W3 = np.random.randn(self.hiddennodes2, self.outputnodes)


    #forward propagation
  def forward(self, X):
    self.z = np.dot(X, self.W1)
    self.z2 = self.sigmoid(self.z)
    self.z3 = np.dot(self.z2, self.W2)
    self.z4 = self.sigmoid(self.z3)
    self.z5 = np.dot(self.z4,self.W3)
    o = self.sigmoid(self.z5)
    return o 

    #activation
  def sigmoid(self, s):
    return 1/(1+np.exp(-s))
    
NN = Neural_Network()

#defining our output 
o = NN.forward(X)

print "Predicted Output: \n" + str(o) 
print "Actual Output: \n" + str(y) 
