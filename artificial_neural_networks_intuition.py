# -*- coding: utf-8 -*-
"""Artificial Neural Networks - Intuition

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WxXRE3akU8U_P-TkIgTgYoH83JLcCmPJ

## Artificial Neural Networks

The artificial neural networks (ANN) are a very powerful structure that imitates the human brain with its neurons. They can do many tasks, such as classification with multiple answers, regressions, interact with environment, play games etc. What will change given the problem is the architecture and the operations from the neural network.

The basic structure for ANN is:

* **Input layer:** Get the i**nputs from our problem. Not all inputs are activated simultaneously.** Each input corresponds to a feature from our dataset, for example if an image has a size of 30 x 30, all the pixels will be transformed as a 2-D matrix and will serve as inputs for our network.

* **Hidden layer:** Make the calculations given the actions by the inputs. It will **perform a weighted sum from the all neurons in the input** (activated or not) and provide some answer. Here that lives the intelligence from the model. For example, the hidden layer will get the picture and try to combine the features by detecting general patterns (edges, textures, lines etc). Each layer on the hidden layer to combine even more with more complexity (shadows, circles etc). Moreover, which more hidden layers we have, more details we will have as well as more computing will be required.

* **Output layer:** Apply the **output for our model given the calculations**. For example, look the top neuron from the last hidden layer and then take the decision, is a cat or not.

The input layer will activate the neurons in the hidden layer that will provide an answer for our problem. The magic is: **Not all connections are activated simultaneously!** This represents that for each step in our learning, the connections will be switched and then we will get better fit for our problem. Each step this connections get even more strong. **This strength will be our weight in the neural network.**

### How the learning happens?

Neural pathways are strenghten every time they are used. If two neurons fire at same time, they the connection between them is enhanced. In our example if two neurons in the input layer provide better results when activated for a specific problem, the connection between is enchanced. Consequently the guesses for our output are enhanced as well.

Another example to make it clear, imagine that you are learning some foreign language, such as Japanese. When you come across come japanese text and try to speak, some connections between your brain are activated and becomes stronger and get easier to remember the words by activating neurons again and again. Get stronger in our case is strenght the weights from our neural network.

In other words: **Practice leads to Perfection!**

## Neural Networks x Classical Machine Learning

In the **classical machine learning models**, **we choose which features will be used** and similarly **what to do with these features** (should add them, combine, multiply etc.). When working with Naive Bayes, our features are words in our emails, and we extracted to make predictions given the probabilities. These approaches are called **Shallow Learning Algorithms**.




* **Shallow Learning**: In this approach the data scientist, machine learning engineer will **choose which feature will help us make sense of data and hence better predictions**. In regression we determine the tetha values, in Naive Bayes the probabilities to be spam or not spam. The trick is **understand the relations between our variables in order to get better predictions.**

* **Deep Learning**: Alternatively, in this approach the **neural network will choose which features make sense**.It means that the neural network will learn from the data by itself regardless of whether you've got a linear or non-linear relation in the most effective way.

Example: In an image recognition problem, you just input images from cat and not cats, hence the neural network will check for the features in order to identify if it is a cat or not.

## How AI Learns? 

### Activation Functions

In the hidden layer, many calculations will be performed by our neurons in order to provide an answer. In order to create the calculus, we will use **functions that will be responsible to dispatch the weights and get our answer stronger (activation function)**. **Depending on which type of problem we are dealing with, a specific type of function is the best fit**. Consequently depending on the value of the weights (strength) calculated of each connection this will correspond to an output for our neural network.

Below you will find some type of activation functions commonly used:

* Binary problems (Yes/No): ReLU

* Probabilities (70% of being fraud): Sigmoid

### Backpropagation

After our prediction, classification, or task is made our **output layer will update the previous hidden layer to correct and adjust the errors** with the reality. The other hidden layers will do the same operation like a backwards cascade effect.**Thus step is called backpropagation!** With the interactions our network will become better given this fine tunning! Each node updates its error from the output to the input like a domino effect updating all errors. **The weights are adjusted depending on the slope of the loss / error function, or the Gradient of the slope**!

### Disadvantages of Neural Networks

* **High power of computing required:** Some times our model will need hours to calculate. Sometimes requires GPU! depending on your parameters.

* **Amount of data required:** If your model is so much complex, you will need more data in order to the get good results.

* **Black-box nature:** This leads for lack of transparency in why the neural network took that decision. Imagine if you are designing something for the legal system, you need to explain why! You can use some techniques that help in this scenario.

**Important: Simpler model = Better results!**

Before we start and create our own neural network. Let's learn using a pre trained model !
"""

# Neural Nets - Pretrained Image Classification

import numpy as np
import tensorflow as tf
import keras

from keras.preprocessing.image import img_to_array, load_img # Image Pre-Processing
from keras.applications.inception_resnet_v2 import InceptionResNetV2 # Convolutional Neural Network - InceptionResNetV2
from keras.applications.inception_resnet_v2 import decode_predictions # After predict, we need to decode into a understandable format
from keras.applications.inception_resnet_v2 import preprocess_input as preprocess_inceptionresnet # This function will help us to make better preprocessing for a better prediction!


from keras.applications.vgg19 import VGG19 # CNN - VGG19
from keras.applications.vgg19 import decode_predictions as decode_predictions_vgg19
from keras.applications.vgg19 import preprocess_input as preprocess_vgg19


# NOTE: All images in this notebook where manually uploaded! Use Google Drive to make them static

# Constants

FILE_1 = '01 Umbrella.jpg'
FILE_2 = '02 Couple.jpg'
FILE_3 = '03 Ocean.jpg'
FILE_4 = '04 Horse.jpg'
FILE_5 = '05 City.jpg'
FILE_6 = '06 Feet.jpg'
FILE_7 = '07 Stairs.jpg'
FILE_8 = '08 Doorway.jpg'
FILE_9 = '09 Ice Cream.jpg'
FILE_10 = '10 Red Shoes.jpg'
FILE_11 = '11 Shoe.jpg'

# 1. Preprocessing Images
# We will convert the images as an array of numbers! 
# Our neural network only understand numbers, so we will use every single pixel as a number
# The dimension of this array will be height x width x channels (r,g,b)

picture = load_img(FILE_1, target_size=(299, 299)) # Load our file with a new 299 x 299 shape (minium required for our NN)
display(picture) #IPython native display

picture_array = img_to_array(picture)
picture_array.shape # 256, 256, 3 >> Height x Width x Channels (3 - Red, Green, and Blue)

# In order to use the inception CNN, we need to adjust our array from 3D to 4D array

expanded_picture = np.expand_dims(picture_array, axis=0)
expanded_picture.shape

# Finishing our image preprocessing with Keras
preprocessed_picture = preprocess_input(expanded_picture)

# 2. Loading our Convolutional Neural Network - InceptionResNetV2

inception_model = InceptionResNetV2(weights='imagenet') # Download all weights pre-trained and apply to Inception model

# Graph is the key on tensorflow!
# Keras will provide the neural network schema and tensorflow will organize all calculus in models using a graph.
# A node will be the inputs, other one the hidden layers etc.  
inception_model.graph = tf.compat.v1.get_default_graph() # course was tf.get_default_graph()

# 3. Making predictions

prediction = inception_model.predict(preprocessed_picture) # Make a prediction given our image 
decode_predictions(prediction) # Decode into an understandable format

# Let's define a function to load and make all image preprocessing
def format_image_inceptionresnet(filename):

  # Load image adjusting the minimum size
  picture = load_img(filename, target_size=(299, 299))

  # Convert an image to an array
  picture_array = img_to_array(picture)

  # Expand dimensions for the minimum 4-D array
  expanded_picture = np.expand_dims(picture_array, axis=0) # We can check if this array is already 4-D and skip this step

  # Pre-Process our image using Keras Preprocessing and returns
  return preprocess_inceptionresnet(expanded_picture)

# Testing with another image and make predictions

picture_2 = format_image_inceptionresnet(FILE_2)
prediction_2 = inception_model.predict(picture_2)
decode_predictions(prediction_2)

# VGG19 - Visual Geometry Group - Cornell University

# Set up VGG19 model
vgg19 = VGG19(weights='imagenet')

def format_image_VGG19(filename):

  # Load image adjusting the minimum size
  picture = load_img(filename, target_size=(224, 224))

  # Convert an image to an array
  picture_array = img_to_array(picture)

  # Expand dimensions for the minimum 4-D array
  expanded_picture = np.expand_dims(picture_array, axis=0) # We can check if this array is already 4-D and skip this step

  # Pre-Process our image using Keras Preprocessing and returns
  return preprocess_vgg19(expanded_picture)

# Let's test VGG19 vs InceptionResNetv2 with the same picture 

picture_2 = format_image_VGG19(FILE_2)
decode_predictions_vgg19(vgg19.predict(picture_2))

