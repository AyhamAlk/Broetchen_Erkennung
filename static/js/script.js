document.getElementById('uploadButton').addEventListener('click', function() {
    document.getElementById('fileInput').click();
});

document.getElementById('fileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const formData = new FormData();
        formData.append('image', file);

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(`Fehler: ${data.error}`);
            } else {
                // Ergebnisse anzeigen
                document.getElementById('result').style.display = 'block';
                document.getElementById('uploadedImage').src = data.image_url;
                document.getElementById('resultText').textContent = data.result;
            }
        })
        .catch(error => {
            console.error('Fehler beim Hochladen:', error);
        });
    }
});
