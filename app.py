from flask import Flask, render_template, request
import analyze_image  # Optional: Falls du ein externes Skript für die Bildanalyse hast

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            # Hier kommt dein Bildanalyse-Code hin
            result = analyze_image.analyze(file)  # Beispiel für die Bildanalyse
            return f"Ergebnis der Analyse: {result}"
    return "Fehler beim Hochladen des Bildes."

if __name__ == "__main__":
    app.run(debug=True)
