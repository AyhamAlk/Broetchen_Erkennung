from flask import Flask, render_template, request, url_for, redirect, jsonify
import os

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
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Dummy Ergebnis zurückgeben und hochgeladenes Bild anzeigen
        return jsonify({
            'image_url': url_for('static', filename='uploads/' + file.filename),
            'result': "Dummy Ergebnis"
        })

if __name__ == '__main__':
    app.run(debug=True)
