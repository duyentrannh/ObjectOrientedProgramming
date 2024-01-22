"""
This code consists of a superclass, DataLoader, with two subclasses.
The main purpose of the code is to load the data and perform necessary adjustments 
to the data can be used for developing neural networks. Inheritance, polymorphism and inheritance
is used in such a way to ensure that common methods for dataloading are employed in the superclass, 
whilst more specific methods regarding each dataset is applied in the subclasses. For instance, the MNIST
dataset requires certain adjustments that will applied only in its specific subclass. 
"""



############### Importing libraries ################

import tensorflow as tf
import numpy as np


############## Superclass DataLoader #################

##
# I start by creating a superclass, DataLoader 
# x_test and x_train needs to be transformed 
# This is needed for both datasets
# Therefore, I create them as instance variables in the constructor 
#
class DataLoader:

  def __init__(self): #initialize constructor
    #I reshape certain variables in the constructor because I dont want them to become overridden 
    # Normalization [0:255] -> [0:1]
    self.x_train = self.x_train / 255
    self.x_test = self.x_test / 255
    # Casting to float32
    self.x_train = self.x_train.astype(np.float32)
    self.x_test = self.x_test.astype(np.float32)

##
# The x_train and x_test have been reshaped in the constructor, but they are not accessed through decorators 
# y_test and y_train are also acccessed through decorators, but they need some additional reshaping 
# 
  @property
  def x_tr(self):
    # @return self.x_train returns the reshaped x_training 
    return self.x_train


  @property
  def x_te(self):
    # @return self.x_test returns the reshaped x_test
    return self.x_test

 #both datasets have 10 classes, either 0-9 or 10 different categories
  @property
  def y_tr(self):
    # @return reshaped y_training as a one-hot-encoder 
    return tf.keras.utils.to_categorical(self.y_train, num_classes = 10, dtype = 'float32')
   

  @property
  def y_te(self):
    # @return reshaped y_test as a one-hot-encoder 
    return tf.keras.utils.to_categorical(self.y_test, num_classes = 10, dtype = 'float32')

    """
    @x: numpy array
    @y: numpy array
    @return: tf data loader object
    """
  # a common method to load a tuple for training set
  def loader(self, batch_size):
    tf_dl = tf.data.Dataset.from_tensor_slices((self.x_tr, self.y_tr)).shuffle(self.x_tr.shape[0]).batch(batch_size)
    return tf_dl

####################### Subclass MNIST ####################


class MNIST(DataLoader): #subclass MNIST inherits from DataLoader
  def __init__(self): #create a constructor 
    (self.x_train, self.y_train), (self.x_test, self.y_test) = tf.keras.datasets.mnist.load_data() #loading MNIST dataset
    super().__init__() #calling superclass constructor 


##
#For specifically MNIST, we want to reshape the training set to 60_000, 784
#These two methods override those in the superclass
  @property
  def x_tr(self):
    #returns a reshaped version of x_train
    return self.x_train.reshape(-1, 28 * 28)

 #reshaping test set to 10000, 784
  @property
  def x_te(self):
    #returns a reshaped version of x_test
    return self.x_test.reshape(-1, 28 * 28)
  
######################### Testing MNIST ###################

#mnist_dataset = MNIST()
#print(mnist_dataset.x_tr.shape, mnist_dataset.y_tr.shape)
#print(mnist_dataset.x_te.shape, mnist_dataset.y_te.shape)

#print(mnist_dataset.x_tr.min(), mnist_dataset.x_tr.max(), mnist_dataset.x_tr.dtype)
#print(mnist_dataset.y_train[2])
#print(mnist_dataset.y_tr[2])


######################## Subclass CIFAR10 ##################

##
# The subclass, CIFAR10 is simply and only inherits all methods from superclass without adding anything extra
# The only thing different is that it loads correct data in the constructor 
class CIFAR10(DataLoader): #Inherits from DataLoader
  def __init__(self): #creating constructor
    (self.x_train, self.y_train), (self.x_test, self.y_test) = tf.keras.datasets.cifar10.load_data() #loading CIFAR10 data
    super().__init__() #callind superclass constructor 
    

####################### Testing CIFAR10 ####################

#cifar10_dataset = CIFAR10()
#print(cifar10_dataset.x_tr.shape, cifar10_dataset.y_tr.shape)
#print(cifar10_dataset.x_te.shape, cifar10_dataset.y_te.shape)

#print(cifar10_dataset.x_tr.min(), cifar10_dataset.x_tr.max())
#print(cifar10_dataset.y_train[2])
#print(cifar10_dataset.y_tr[2])