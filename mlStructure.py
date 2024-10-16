import tensorflow as tf
from tensorflow import keras
import xml.etree.cElementTree as ET
import os
import numpy as np

def load_dataset(images_dir, annotations_dir):
    images = []
    labels = []
    for filename in os.listdir(images_dir):
        if filename.endswith(('.png','.jpg')):
            img_path = os.path.join(images_dir, filename)
            xml_path = os.path.join(annotations_dir,filename[:-4] + '.xml')

            # load image
            img = tf.keras.preprocessing.image.load_img(img_path)
            img = tf.keras.preprocessing.image.img_to_array(img)
            images.append(img)

            # Parse annotations (replace with your annotation format)
            tree = ET.parse(xml_path)
            root = tree.getroot()
            boxes = []
            classes = []
            for obj in root.findall('object'):
                xmin = int(obj.find('bndbox').find('xmin').text)
                ymin = int(obj.find('bndbox').find('ymin').text)
                xmax = int(obj.find('bndbox').find('xmax').text)
                ymax = int(obj.find('bndbox').find('ymax').text)
                boxes.append([xmin, ymin, xmax, ymax])
                classes.append(obj.find('name').text)
            labels.append({'boxes': np.array(boxes), 'classes': np.array(classes)})

    return np.array(images), np.array(labels)


def build_model(images_dir, annotations_dir):
    # Load the dataset
    images, labels = load_dataset(images_dir, annotations_dir)

    # Preprocess the data (normalize pixel values)
    images = images / 255.0

    # Create a simple object detection model
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 3)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation = 'relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    # Set number of labels (classes)
    tf.keras.layers.Dense(22, activation = 'softmax')])

    # Compile the model
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    # Convert labels to a suitable format for the model
    y_train = np.array([label['classes'][0] for label in labels])  # Assuming one object per image

    # Resize images to match the model's input shape
    resized_images = tf.image.resize(images, (256, 256))

    # Train the model
    #model.fit(resized_images, y_train, epochs=10)
    model.save('my_model.h5')
    print("successfully built model")
