from flask import Flask, render_template, request
import os
from analyze_image import analyze

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            # Bild analysieren
            result = analyze(file.stream)
            filename = file.filename
            return render_template('result.html', filename=filename, result=result)
    return "Fehler beim Hochladen des Bildes."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
