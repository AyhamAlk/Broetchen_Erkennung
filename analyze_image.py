# analyze_image.py
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Modell laden
model = load_model('model.h5')

# Funktion zur Bildanalyse
def analyze(image_stream):
    # Bild laden
    img = Image.open(image_stream)
    img = img.resize((224, 224))  # Bild auf die Größe anpassen, die das Modell erwartet
    img_array = np.array(img) / 255.0  # Normalisierung der Pixelwerte
    img_array = np.expand_dims(img_array, axis=0)  # Batch-Dimension hinzufügen

    # Vorhersage mit dem Modell
    predictions = model.predict(img_array)
    
    # Kategorisierung anhand der Vorhersage
    categories = ['Kategorie 1', 'Kategorie 2', 'Kategorie 3']  # Füge hier deine Kategorien ein
    predicted_category = categories[np.argmax(predictions)]
    
    return predicted_category
