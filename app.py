import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from flask import Flask, render_template, request, url_for, jsonify
from werkzeug.utils import secure_filename
import os

# Lade das Modell
model = tf.keras.models.load_model('model.h5')

def analyze(img_stream):
    # Bereite das Bild vor
    img = image.load_img(img_stream, target_size=(224, 224))  # Anpassen an die Größe deines Modells
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Batch-Dimension hinzufügen

    # Normalisiere das Bild (falls erforderlich)
    img_array /= 255.0

    # Vorhersage machen
    predictions = model.predict(img_array)
    
    # Ergebnisse zurückgeben
    return predictions

# Initialisiere die Flask-App
app = Flask(__name__, template_folder='templates', static_folder='static')

# Upload-Verzeichnis für Bilder
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'Keine Datei gefunden!'}), 400
    
    file = request.files['image']
    
    if file.filename == '':
        return jsonify({'error': 'Keine Datei ausgewählt!'}), 400
    
    if file:
        filename = secure_filename(file.filename)  # Sicheren Dateinamen generieren
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        # Führe die Bildanalyse durch
        try:
            result = analyze(filepath)

            # Angenommen, du hast nur zwei Klassen: 'Brötchen_A' und 'Brötchen_B'
            class_names = ['Wikingerbrötchen', 'Weltmeisterbrötchen']
            
            # Berechne die Wahrscheinlichkeit für die erste Klasse
            first_class_probability = result[0][0] * 100  # Beispiel für die erste Klasse

            return jsonify({
                'image_url': url_for('static', filename='uploads/' + filename),
                'result': f"{class_names[np.argmax(result)]}: {first_class_probability:.2f}%"  # Klasse und Wahrscheinlichkeit formatieren
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500  # Gibt die Fehlermeldung zurück

if __name__ == '__main__':
    app.run(debug=True)
