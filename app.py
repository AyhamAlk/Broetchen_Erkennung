from flask import Flask, render_template, request, url_for, redirect
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
    # Prüfen, ob eine Datei im Formular enthalten ist
    if 'image' not in request.files:
        return redirect(request.url)
    
    file = request.files['image']
    
    # Prüfen, ob ein Dateiname existiert
    if file.filename == '':
        return redirect(request.url)
    
    # Datei speichern und Pfad erstellen
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Dummy Ergebnis zurückgeben und hochgeladenes Bild anzeigen
        return render_template('index.html', image_url=url_for('static', filename='uploads/' + file.filename), result="Dummy Ergebnis")

if __name__ == '__main__':
    app.run(debug=True)
