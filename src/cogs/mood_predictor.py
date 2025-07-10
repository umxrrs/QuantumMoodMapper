import tensorflow as tf
import numpy as np

class MoodPredictor:
    def __init__(self):
        self.model = tf.keras.models.load_model('config.json')['model_path'])
        self.moods = ['calm', 'energetic', 'sad', 'happy']

    def predict(self, features):
        features = np.expand_dims(features, axis=0)
        prediction = self.model.predict(features)
        return self.moods[np.argmax(prediction)]
