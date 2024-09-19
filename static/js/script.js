document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Verhindert das Standard-Formular-Submit-Verhalten

    let formData = new FormData(this);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Zeigt das Ergebnis auf der Seite an
        document.getElementById('result').style.display = 'block';
        document.getElementById('resultText').textContent = data.result;
        document.getElementById('uploadedImage').src = data.image_url;
    })
    .catch(error => {
        console.error('Fehler beim Hochladen:', error);
    });
});
