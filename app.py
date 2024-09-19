from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

UPLOAD_FOLDER = os.path.join('static', 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if request.method == 'POST':
            file = request.files['image']
            if file:
                filepath = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(filepath)
                
                # Dummy-Ergebnis für die Bildanalyse
                dummy_result = "Dies ist ein Test-Ergebnis."

                # Weiterleiten zu /result mit Bild-URL und Ergebnis
                return jsonify({
                    'result': dummy_result,
                    'image_url': f'/static/uploads/{file.filename}'
                })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'error': 'Fehler beim Hochladen'}), 400

@app.route('/result')
def result():
    image_url = request.args.get('image_url')
    result = request.args.get('result')
    return render_template('result.html', image_url=image_url, result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
