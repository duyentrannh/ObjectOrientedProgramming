"""
This code uses argparse to provide user-friendly command-line interfaces.
First, it provides a brief description of the program, the dataset and some key methods.
The user will also be provided with two examples of how to run the code in the terminal.
The user must specify certain parameters. Some are required, other have defaults or can be changed. 
Based on these input parameters, the program will create, train and test a neural network based on 
one of the datasets. Lastly, the user will be provided with the loss function for each epoch or step,
and Area under the ROC curve (AUC) estimation, indicating the performance of the model.  
"""


###################### Importing libraries ######################


from neuralnetwork import NeuralNetwork, FullyConNN, ConvNN
from dataloader import DataLoader, MNIST, CIFAR10
from sklearn.metrics import roc_auc_score
import tensorflow as tf
import argparse
import textwrap
import numpy as np


######################### Argparse ################################

##
#I create an argparse object
#I use prog for the program name, a description of what the program does and epilog or a text at the bottom of help
#I provide a brief description of the neural networks and datasets
#I also provide a description of some of the key methods used in the program
#Lastly, we provide two examples of how the user can run the code from the terminal 
#

parser = argparse.ArgumentParser(prog='This is a training program for neural networks',
                                formatter_class=argparse.RawDescriptionHelpFormatter,
                                description=textwrap.dedent('''\
                                                 Neural Networks
                                     --------------------------------
                                     This is a program developed to create, train and test neural networks. 
                                     In this program, we are working with two types of neural networks, both intended
                                     to classify pictures. 
                                                            
                                     The fully connected neural network is intended to use on the MNIST dataset. MNIST is a 
                                     dataset of handwritten digits in black and white, ranging from 0 to 9. 
                                     60 images are used for training and 10 000 images are used for testing. 
                                                            
                                     The convolutional neural network is intended to use on the CIFAR10 dataset. 
                                     CIFAR10 is a dataset of colour images with a total of 10 different classes, such as airplane, 
                                     bird, cat, ship etc. 50 000 images are used for training and 10 000 images are used for testing.
                                                            
                                                              Some key methods included:
                                                            
                                     1) __repr__ : Provides a string representation of a class in a neural network
                                     @return: description of class(NeuralNetwork, FullyConNN, ConvNN) in string format
                                                            
                                     2)hidden_layers : Defined and return the network with hidden layers. Varies depending on neural network.                                                
                                     FullyConNN : @return: returns a neural network with one input layer and two fully connected('Dense')
                                                layers with a number of neurons.
                                     ConvNN : @return: a neural network with input layer and three Conv2D layers with different 
                                                configurations(filters, kernel_size, strides, neurons).                                                                                          
                                                The last layer 'flattens' the ouput from previous Conv layer, making it suitable for outputting predictions.
                                                            
                                     3)classifier : to create a classifier part of neural network for making final predictions.                       
                                     @return: a 'Sequential' model with input layer = neurons and dense layer (y_dim units and 
                                            activation function : softmax(convert the raw ouput into probabilities)) 

                                     4)call : Performs a call through the network and compute the loss for training purpose.
                                     @return: the calculated cross entropy loss that will used during the training process of neutral network.
                                                            
                                     5)test: Performs a test using test data x.
                                     @return (pseudo) probabilities which sum up to 1 and raw output probabilities from the classifier                                             

                                     6)train : Performs training step(repeatedly) on each batch of inputs, apply call method 
                                            to compute the loss, form that compute the gradients and update the model using optimizer.
                                     @return: the calculated loss for current training step. This loss can be used for the training progress.

                                     7)loader : Creates a data loader for training data( x_tr and y_tr)
                                     @return : the Tensorflow data loader object
                                                                                                                                                                        
                                     '''),
                                     epilog=textwrap.dedent('''\
                                                USAGE
                                     -------------------------------- 

                                     Example 1: Run this line to develop, train and test a fully connected neural network on the MNIST dataset with 10 epochs.
                                     OBS: You are required to choose dset and nn_type. Other parameters have default values but can be changed.                   
                                     python3 train.py --dset MNIST --nn_type FullyConNN --epochs 10

                                     Example 2: Run this line to develop, train and test a convolutional neural network on the CIFAR10 dataset with 10 epochs.
                                     OBS: You are required to choose dset and nn_type. Other parameters have default values but can be changed.
                                     python3 train.py --dset CIFAR10 --nn_type ConvNN --epochs 10                                                                                                                 
                                    
                                     ''')
                    )


##
# I add all necessary arguments 
# To ensure that the code will run as excpected, I try to explicate which variables are required, what their type is and provide defaults 
#
parser.add_argument('--dset', choices = ['MNIST', 'CIFAR10'], required = True, type = str, help = "Specify whether you want to use MNIST or CIFAR10")
parser.add_argument('--nn_type', choices = ['FullyConNN', 'ConvNN'], required = True, type = str, help = "Specify whether you want to use a fully connected neural network (FullyConNN) or Convolutional neural network (ConvNN)")
parser.add_argument('--epochs', default = 10, type = int, help = 'specify the numbers of epochs you want to use to train your neural network')
parser.add_argument('--neurons', default = 50, type = int, help = "Specify the number of neurons to use in your neural network")
parser.add_argument('--batch_size', default = 256, type = int, help = "Specify the batch size used in the optimization routine")


##
#To go even further to ensure that inputs are correct, I provide try-expects 
#For instance, certain values cannot be negative
#Or certain neural networks are intended to use with certain datasets
#
try:
    args = parser.parse_args() #We pass all arguments into an object that retrieve the arguments

    if args.epochs < 1:
        raise ValueError("Number of epochs must be at least 1.")
    if args.neurons < 1:
        raise ValueError("Number of neurons must be at least 1.")
    if args.batch_size < 1:
        raise ValueError("Batch size must be at least 1.")
    if args.dset == 'MNIST' and args.nn_type == 'ConvNN':
        raise ValueError("The convNN is intended for the CIFAR10 dataset.")
    if args.dset == 'CIFAR10' and args.nn_type == 'FullyConNN':
            raise ValueError("The FullyConNN is intended for MNIST")
        
except ValueError as error:
    print("Got an error: ", error)
        
##
# Neural network and dataset initialization
#
if args.nn_type == 'FullyConNN':
    model = FullyConNN(input_shape=(784), neurons=args.neurons)
elif args.nn_type == 'ConvNN':
    model = ConvNN(input_shape=(32, 32, 3), filters=32, kernel_size=3, strides=(2, 2), neurons=args.neurons)

if args.dset == 'MNIST':
     data_loader = MNIST()
elif args.dset == 'CIFAR10':
    data_loader = CIFAR10()

##
# Get the data loader object for training
# The batch_size provided in the argparse will be passed to the loader method in DataLoader
train_data_loader = data_loader.loader(batch_size=args.batch_size)


##
# Optimizer to minimize loss function in training
# # i need to add 'legacy' because on my Macbook M1/M2 the terminal requires it 
optimizer = tf.keras.optimizers.legacy.Adam(learning_rate=5e-4)

## 
# Training loop
# Besides what was stated in the assignment, I have added a loss list to explicitly see how much the loss 
# reduces for each step/epoch.
# This is very valuable information, as a well functioning neural network would indicate a declining loss for each step/epoch.
#
step = 0
while step < args.epochs :
    losses = [] #creating a list
    for i, data_batch in enumerate(train_data_loader):
        loss = model.train(data_batch , optimizer)
        losses.append(loss) #appending the losses to the list for each time
    
    losses = np.array(losses).mean()
    print(f'Epoch: {step} - Loss: {losses:0.4f}')
    step +=1


# AUC calculation
# Assuming model.test method exists and returns predictions
pi_hat = model.test(data_loader.x_te)
y_te = data_loader.y_te
print("Shape of y_te:", y_te.shape)
y_hat, pi_hat = model.test(data_loader.x_te)
print("Shape of pi_hat:", pi_hat.shape)
auc = roc_auc_score(y_te, pi_hat)
print('Final AUC %0.4f' % auc)







