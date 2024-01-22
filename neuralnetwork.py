"""
This code consists of a superclass for NeuralNetwork, which has two subclasses.
The subclass FullyConNN is a subclass for fully connected layers neural network.
The subclass ConvNN is a subclass for convolutional neural network. 
The overall aim of this code is to use inheritance, polymorphism and overriding in a way that
enables us to strategically and effectively share the methods that are common for both subclasses
in the superclass, whilst certain specific method are either developed or overridden in the subclass.
For instance, methods for classifying, training and testing are common for both neural networks and developed in superclass,
whereas the specific way hidden layers are developed will vary depending on the type of neural network at hand. 
"""


################### Importing libraries #########################
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential


####################### Superclass NeuralNetwork ##################

##
# We create a superclass, although our superclass originally inherits from tf.keras.Model
# We create a constructor for the superclass that takes in certain parameters
# We also call the superclass constructor of tf.keras.Model which it inherits from
# Lastly, we assign the input paraemters are instance variables 
# @param input_shape takes in the shape of the instances 
# @param neurons takes in the number of neurons used for layers
# @param y_dim takes in number of output neurons in the dense layer for classification
#
class NeuralNetwork(tf.keras.Model):
  def __init__(self, input_shape, neurons: int = 50, y_dim: int = 10): #default values
    super().__init__()
    self._input_shape = input_shape
    self._neurons = neurons
    self._y_dim = y_dim 

##
#Creating instance variables based on instances of the hidden_layer and classifier methods
#The method hidden_layer will depend on whether FullyConNN or ConvNN is initialized 
#
    self._hidden = self.hidden_layers()
    self._classifier = self.classifier()

##
#The assignment provides a code for param which is to be used both in the constructor for FullyConNN and ConvNN
#Since this code is common and would be repeated, I choose to use this is the constructor instead
#However, I use self instead so it will adapt to the specific type of neural network at hand
#
    self._params = self._hidden.trainable_variables + self._classifier.trainable_variables


##
# A common method, but it will be overriden in subclass
# repr is in-build
#@return a description of the class in string format
#
  def __repr__(self):
    return "This as a Neural Network."

##
#An abstract method
#I specify it in the superclass, but will implement it later in subclass 
#both subclasses will have a method for hidden layer, but exactly how they are developed will differ
#
  def hidden_layers(self):
    raise NotImplementedError

##
#A common method
#Dense layers are used for FullyConNN
#However, both FullyConNN and ConvNN will end up using it in the last classification part
#Therefore, this method is common
#
  def classifier(self):
    return Sequential([layers.InputLayer(input_shape = self._neurons),
                      layers.Dense(self._y_dim, activation='softmax')])

##
#A common method
#@param x takes in input data
#@param y takes in label 
#@return loss returns the calculated loss entropy function 
#  
  def call(self, x, y):
    out = self._hidden(x)
    out = self._classifier(out)
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y, out))
    return loss

##
#A common method for training 
#@param inputs are assigned as (x,y)
#@params optimizer is already defined using Adam to minimize loss
#@return loss after gradient
#
  def train(self, inputs, optimizer = tf.keras.optimizers.Adam(learning_rate = 5e-4)):
    x, y = inputs
    with tf.GradientTape() as tape:
      loss = self.call(x, y)
      gradients = tape.gradient(loss, self._params)
      optimizer.apply_gradients(zip(gradients, self._params))
      return loss

##
#A common method for testing 
#@param x in input data
#@return y_hat returns (pseudo)probabilities ranging from 0 to 1
#@return pi_hat returns the output of the classifier, the raw probabilities
#

  def test(self, x):
    out = self._hidden(x) #create out, an instance of the self method hidden with dataset x as an argument 
    out = self._classifier(out) #we pass out as an argument in the self method classifier 
    pi_hat = out #the output of the classifier is all probabilities, called pi_hat
    y_hat = tf.math.argmax(out,1) #argmax gives biggest (pseudo)probabilities from 0-1
    return y_hat,pi_hat


################# Subclass FullyConNN ###############

##
# We create a subclass FullyConNN 
# @param input_shape takes in the shape of the instances 
# @param neurons takes in the number of neurons used for layers
# @param y_dim takes in number of output neurons in the dense layer for classification
#

class FullyConNN(NeuralNetwork): #subclass FullyConNN inherits from superclass NeuralNetworks
  def __init__(self, input_shape = (28*28), neurons = 50, y_dim = 10): #default values
    super().__init__(input_shape, neurons, y_dim) #superclass constructor is called with its own input parameters 


##
# We take the abstract method hidden_layers mentioned in superclass and implement it 
# Specifically, since this is a fully connected NN, we add dense layers 
# @returns the fully connected network
  def hidden_layers(self):
    return Sequential([layers.InputLayer(input_shape=self._input_shape),
                       layers.Dense(self._neurons),
                       layers.Dense(self._neurons)])


##
# repr was mentioned in superclass and overriden here with more specific information
# @returns doc string
  def __repr__(self):
    return f"This is a fully connected neural network with input_shape: {self._input_shape}, neurons: {self._neurons}, and y_dim: {self._y_dim}."
  
################### Subclass ConvNN ######################


## 
# we create a subclass for ConvNN
# @param input_shape takes in the shape of the instances 
# @param neurons takes in the number of neurons used for layers
# @param filters takes in number of output filters
# @param kernel_size takes in size of convolution window/kernel
# @param strides takes in strides of the convolution, height and width
#
class ConvNN(NeuralNetwork): #subclass ConvNN inherits from superclass NeuralNetwork
  def __init__(self, input_shape, neurons = 50, filters = 32, kernel_size = 3, strides = (2,2)): #default values
    self._filters = filters
    self._kernel_size = kernel_size
    self._strides = strides
    super().__init__(input_shape, neurons) #superclass constructor is called, but after instance variables are assigned

##
# The abstract method hidden_layer is implemented specifically for ConvNN subclass
# @returns the convolutional neural network
#
  def hidden_layers(self):
    return Sequential([layers.InputLayer(input_shape=self._input_shape),
                        layers.Conv2D(filters=self._filters, kernel_size=self._kernel_size, strides=self._strides),
                        layers.Conv2D(filters=2 * self._filters, kernel_size=self._kernel_size, strides=self._strides),
                        layers.Conv2D(filters=self._neurons, kernel_size=self._kernel_size, strides=(5, 5)),
                        layers.Flatten()])
  
 
 ##
 # repr is overriden 
 # @returns the relevant information 
  def __repr__(self):
    return f"This is a fully connected neural network with input_shape: {self._input_shape}, neurons: {self._neurons}, filters: {self._filters}, kernel_size: {self._kernel_size}, and strides: {self._strides}."


################ Testing ###############

#fully_connected_layer = FullyConNN(input_shape=(28, 28), neurons=50, y_dim=10)
#print(fully_connected_layer._hidden)

#noise = tf.random.uniform(shape=(28, 28))
#fully_connected_layer.test(noise)

