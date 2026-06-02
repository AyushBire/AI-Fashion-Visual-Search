import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np

model = ResNet50(weights='imagenet',
                 include_top=False,
                 pooling='avg')

def extract_features(img_path):

    img = image.load_img(img_path,
                         target_size=(224, 224))

    img_array = image.img_to_array(img)

    img_array = np.expand_dims(img_array,
                               axis=0)

    img_array = preprocess_input(img_array)

    features = model.predict(img_array,
                             verbose=0)

    return features.flatten()