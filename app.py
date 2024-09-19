from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')  # Startseite

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if request.method == 'POST':
            file = request.files['image']  # Bild vom Formular abholen
            if file:
                # Speichere das hochgeladene Bild in einem temporären Ordner
                filepath = os.path.join('static/uploads', file.filename)
                file.save(filepath)
                
                # Dummy-Ergebnis für die Bildanalyse
                dummy_result = "Dies ist ein Test-Ergebnis."

                # Leitet zur Ergebnisseite weiter, nachdem das Bild verarbeitet wurde
                return render_template('result.html', filename=file.filename, result=dummy_result)
    except Exception as e:
        return f"Ein Fehler ist aufgetreten: {e}", 500

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
