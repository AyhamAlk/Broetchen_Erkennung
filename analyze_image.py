import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Lade das Modell
model = tf.keras.models.load_model('model.h5')
model.summary()

def analyze(img_stream):
    # Bereite das Bild vor
    img = image.load_img(img_stream, target_size=(224, 224))  # Anpassen an die Größe deines Modells
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Batch-Dimension hinzufügen

    # Normalisiere das Bild (falls erforderlich)
    img_array /= 255.0

    # Vorhersage machen
    predictions = model.predict(img_array)

    # Hier definierst du die Klassennamen für dein Modell
    class_names = ['Wikingerbrötchen', 'Weltmeisterbrötchen']

    # Bestimme die Klasse mit der höchsten Wahrscheinlichkeit
    class_index = np.argmax(predictions[0])
    class_name = class_names[class_index]
    
    # Ergebnisse zurückgeben
    return predictions[0][class_index] * 100, class_name  # Rückgabe der Wahrscheinlichkeit und des Klassennamens
