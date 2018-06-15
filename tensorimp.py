import tensorflow as tf


#number of layers and how many nodes in a layer
node_hl1 = 500
node_hl2 = 500
node_hl3 = 500

#output size and batch size
n_classes = 10
batch_size = 100

#input values
x = tf.placeholder('float')
#label
y = tf.placeholder('float')

#Neural network model
def neuralnetmodel(data):

    #Randomizing weights
    hidden_layer1 = {'weights':tf.Variable(tf.random_normal([784,node_hl1])),'biases':tf.Variable(tf.random_normal([node_hl1]))}
    
    hidden_layer2 = {'weights':tf.Variable(tf.random_normal([node_hl1,node_hl2])),'biases':tf.Variable(tf.random_normal([node_hl2]))}
    
    hidden_layer3 = {'weights':tf.Variable(tf.random_normal([node_hl2,node_hl3])),'biases':tf.Variable(tf.random_normal([node_hl1]))}

    output_layer = {'weights':tf.Variable(tf.random_normal([node_hl3,n_classes])),'biases':tf.Variable(tf.random_normal([n_classes]))}

    #forward propagation

    l1 = tf.add(tf.matmul(data, hidden_layer1['weights']), hidden_layer1['biases'])
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(l1, hidden_layer2['weights']), hidden_layer2['biases'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2, hidden_layer3['weights']), hidden_layer3['biases'])
    l3 = tf.nn.relu(l3)

    output = tf.matmul(l3, output_layer['weights']) + output_layer['biases']

    return output


#training
def train_nn(x):
    prediction = neuralnetmodel(x)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits =prediction,labels = y))
    optimizer = tf.train.AdamOptimizer().minimize(cost)

    hm_epochs = 40

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        for epoch in range(hm_epochs):
            epoch_loss = 0
            for _ in range(int(mnist.train.num_examples/batch_size)):
                epoch_x,epoch_y = mnist.train.next_batch(batch_size)
                _,c = sess.run([optimizer,cost],feed_dict = {x: epoch_x, y: epoch_y})
                epoch_loss += c
            print('Epoch', epoch,'completed out of',hm_epochs,'loss:',epoch_loss)
        
        correct = tf.equal(tf.argmax(prediction,1),tf.argmax(y,1))
        accuracy = tf.reduce_mean(tf.cast(correct,'float'))
        print('accuracy : ',accuracy.eval({x:mnist.test.images, y:mnist.test.labels}))

train_nn(x)


