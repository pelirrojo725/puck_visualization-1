#!/usr/local/bin/python3.8
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import cv2
import matplotlib.pyplot as plt
import sys
import numpy as np
from datetime import date

# Setting the default parameters
batch_size = 25
epochs = 43
IMG_HEIGHT = 150
IMG_WIDTH = 150

# Gets rid of the following error message
# I tensorflow/core/platform/cpu_feature_guard.cc:143] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
# I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x7fd5c0d44380 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
# I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Category names for classification
category_names = ['Straight', 'Tilted', 'Empty']


def plotImages(images_arr):  # Method to easily show images to the user
    fig, axes = plt.subplots(1, 5, figsize=(20, 20))
    axes = axes.flatten()
    for img, ax in zip(images_arr, axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.show()


# Normalizing an input image into the proper parameters for predicition
def prepare_image(img_name):
    input_image = cv2.imread(img_name)
    image_resize = cv2.resize(
        input_image, (IMG_HEIGHT, IMG_WIDTH))
    image_resize = image_resize / 255
    image_reshape = image_resize.reshape(
        (1, IMG_HEIGHT, IMG_WIDTH, 3))
    return image_reshape


# Path to main directory containing the images
PATH = os.path.join(os.path.dirname(
    '/home/samuel/Desktop/Classes/CSC_300/puck_visualization_system/puck_visualization_program/var/model_data/'))

# Joining the training and test directories onto the path
train_dir = os.path.join(PATH, 'train')
test_dir = os.path.join(PATH, 'test')

# Adding the categories onto the training images for each condition
train_straight_dir = os.path.join(train_dir, category_names[0])
train_tilted_dir = os.path.join(train_dir, category_names[1])
train_empty_dir = os.path.join(train_dir, category_names[2])

# Getting the number of images for training per directory
num_straight_tr = len(os.listdir(train_straight_dir))
num_tilted_tr = len(os.listdir(train_tilted_dir))
num_empty_tr = len(os.listdir(train_empty_dir))

# Getting the total number of images for training
total_train = num_straight_tr + num_tilted_tr + num_empty_tr

# Adding the categories to the testing images for each condition
test_straight_dir = os.path.join(test_dir, category_names[0])
test_tilted_dir = os.path.join(test_dir, category_names[1])
test_empty_dir = os.path.join(test_dir, category_names[2])

# Getting the number of test images per directory and condition
num_straight_test = len(os.listdir(test_straight_dir))
num_tilted_test = len(os.listdir(test_tilted_dir))
num_empty_test = len(os.listdir(test_empty_dir))

# Getting the total number of test images
total_test = num_straight_test + num_tilted_test + num_empty_test


# An image generator that alters the images to avoid overfitting
image_gen_train = ImageDataGenerator(
    rescale=1. / 255,
    rotation_range=45,
    width_shift_range=.15,
    height_shift_range=.15,
    horizontal_flip=True,
    zoom_range=0.5

)

test_image_generator = ImageDataGenerator(rescale=1. / 255)

# Getting the images from the training directory, altering them, and localizing them for use
train_data_gen = image_gen_train.flow_from_directory(batch_size=batch_size,
                                                     directory=train_dir,
                                                     shuffle=True,
                                                     target_size=(
                                                         IMG_HEIGHT, IMG_WIDTH),
                                                     class_mode='categorical')

# Getting the images from the testing directory and localizing them for use
test_data_gen = test_image_generator.flow_from_directory(batch_size=batch_size,
                                                         directory=test_dir,
                                                         target_size=(
                                                             IMG_HEIGHT, IMG_WIDTH),
                                                         class_mode='categorical')

# Creating the model for training
strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
with strategy.scope():
    model = Sequential([

        Conv2D(256, 3, padding='same', activation='relu',
            input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),

        MaxPooling2D(pool_size=(2, 2)),

        Conv2D(256, 3, padding='same', activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),

        Conv2D(512, 3, padding='same', activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),

        Flatten(),

        Dense(128, activation='relu'),

        Dense(3, activation=tf.nn.softmax)
    ])

    # Compiling the model
    model.compile(optimizer='adam',
                loss=tf.keras.losses.CategoricalCrossentropy(),
                metrics=['accuracy'])


history = model.fit(
    train_data_gen,
    steps_per_epoch=total_train // batch_size,
    epochs=epochs,
    validation_data=test_data_gen,
    validation_steps=total_test // batch_size
)

model_dict = '/home/samuel/Desktop/Classes/CSC_300/puck_visualization_system/puck_visualization_program/models/'
model_name = 'puck_visualization_model_' + date.today().strftime('%b_%d_%Y') + '.h5'
model.save(model_dict + model_name)

# Using np.argmax to get the category number of the input image
# predictions = np.argmax(model.predict([prepare_image(sys.argv[1])]), axis=-1)


# f = open('output.txt', 'a')

# f.write('Prediction for ' + os.path.basename(sys.argv[1]) + ': ')
# f.write(category_names[predictions[0]])
# print(category_names[predictions[0]])
# f.write('\n')

# f.close()
# Ploting the accuracy and loss over the given epochs

# acc = history.history['accuracy']
# val_acc = history.history['val_accuracy']

# loss = history.history['loss']
# val_loss = history.history['val_loss']

# epochs_range = range(epochs)

# plt.figure(figsize=(8, 8))
# plt.subplot(1, 2, 1)
# plt.plot(epochs_range, acc, label='Training Accuracy')
# plt.plot(epochs_range, val_acc, label='Testing Accuracy')
# plt.legend(loc='lower right')
# plt.title('Training and Testing Accuracy')

# plt.subplot(1, 2, 2)
# plt.plot(epochs_range, loss, label='Training Loss')
# plt.plot(epochs_range, val_loss, label='Testing Loss')
# plt.legend(loc='upper right')
# plt.title('Training and Testing Loss')
# plt.show()
