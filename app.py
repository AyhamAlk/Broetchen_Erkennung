from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return redirect(request.url)
    
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        # Speichern der Datei im Upload-Ordner
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        # Dummy Ergebnis anzeigen
        return render_template('index.html', image_url=url_for('static', filename='uploads/' + file.filename), result='Dummy Ergebnis')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
