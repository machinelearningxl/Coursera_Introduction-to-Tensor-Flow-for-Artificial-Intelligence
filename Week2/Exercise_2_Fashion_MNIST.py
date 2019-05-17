# @Author: Antero Maripuu Github:<machinelearningxl>
# @Date : 2019-05-17 19:03
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename : Exercise_2_Fashion_MNIST.py

#In the course you learned how to do classification using Fashion MNIST, a data set containing items of clothing.
# There's another, similar dataset called MNIST which has items of handwriting -- the digits 0 through 9.

#Write an MNIST classifier that trains to 99% accuracy or above, and does it without a fixed number of epochs --
#i.e. you should stop training once you reach that level of accuracy.

#Some notes:

#    It should succeed in less than 10 epochs, so it is okay to change epochs to 10, but nothing larger
#    When it reaches 99% or greater it should print out the string "Reached 99% accuracy so cancelling training!"
#    If you add any additional variables, make sure you use the same names as the ones used in the class

#I've started the code for you below -- how would you finish it?


# YOUR CODE SHOULD START HERE
# YOUR CODE SHOULD END HERE
import tensorflow as tf
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
plt.imshow[x_train[1]]
# YOUR CODE SHOULD START HERE

# YOUR CODE SHOULD END HERE
model = tf.keras.models.Sequential([
    # YOUR CODE SHOULD START HERE

    # YOUR CODE SHOULD END HERE
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# YOUR CODE SHOULD START HERE
# YOUR CODE SHOULD END HERE
plt.show()