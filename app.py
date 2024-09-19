from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder='templates')
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html', image_url=None, result=None)

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return render_template('index.html', image_url=None, result="Kein Bild hochgeladen.")
    
    file = request.files['image']
    if file.filename == '':
        return render_template('index.html', image_url=None, result="Kein Bild ausgewählt.")
    
    if file:
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Dummy-Ergebnis
        dummy_result = "Dies ist ein Dummy-Ergebnis."

        return render_template('index.html', image_url=f"/static/uploads/{filename}", result=dummy_result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
