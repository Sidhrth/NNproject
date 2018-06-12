import numpy as np

#example is housing prices
# X input variables - size, age, distance to market.
X = np.array(([100, 20, 3000], [400, 5, 100], [240, 10, 1000]), dtype=float)
y = np.array(([300], [900], [500]), dtype=float)

# Feature scaling
X = X/np.amax(X, axis=0)
y = y/1000 



class Neural_Network(object):
  def __init__(self):

    self.inputnodes = 3
    self.outputnodes = 1
    self.hiddennodes = 3

    #weights
    self.W1 = np.random.randn(self.inputnodes, self.hiddennodes) 
    self.W2 = np.random.randn(self.hiddennodes, self.outputnodes)


    #forward propagation
  def forward(self, X):
    self.z = np.dot(X, self.W1)
    self.z2 = self.sigmoid(self.z)
    self.z3 = np.dot(self.z2, self.W2)
    o = self.sigmoid(self.z3)
    return o 

    #activation
  def sigmoid(self, s):
    return 1/(1+np.exp(-s))

  def sigmoidPrime(self, s):
    return s * (1 - s)

    #backpropagation
  def backward(self, X, y, o):
    self.o_error = y - o 
    self.o_delta = self.o_error*self.sigmoidPrime(o)
    self.z2_error = self.o_delta.dot(self.W2.T)
    self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2)
    
    
    #optimizing weights
    self.W1 += X.T.dot(self.z2_delta)
    self.W2 += self.z2.T.dot(self.o_delta)

  def train (self, X, y):
    o = self.forward(X)
    self.backward(X, y, o)

NN = Neural_Network()
for i in xrange(1000):
  print "Input: \n" + str(X) 
  print "Actual Output: \n" + str(y) 
  print "Predicted Output: \n" + str(NN.forward(X)) 
  print "Loss: \n" + str(np.mean(np.square(y - NN.forward(X))))
  print "\n"
  NN.train(X, y)  