from flask import Flask, render_template, request
# import analyze_image  # Optional: Falls du ein externes Skript für die Bildanalyse hast
import os

app = Flask(__name__, template_folder='templates')  # Den 'templates'-Ordner korrekt referenzieren

@app.route('/')
def index():
    return render_template('index.html')  # Lädt die Datei 'index.html' aus dem 'templates'-Ordner

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            # Datei im Stream verarbeiten, um Speicher zu sparen
            # result = analyze_image.analyze(file.stream)  # Bildanalyse wird auf den Stream angewendet
            return f"Ergebnis der Analyse:"
    return "Fehler beim Hochladen des Bildes."

if __name__ == "__main__":
    # Debugging deaktiviert für Produktionsumgebung, speicherschonende Einstellungen
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
