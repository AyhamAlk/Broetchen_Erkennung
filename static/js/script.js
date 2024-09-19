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
                // Hier wird die Seite umgeleitet zu /result mit den Ergebnissen
                window.location.href = `/result?image_url=${encodeURIComponent(data.image_url)}&result=${encodeURIComponent(data.result)}`;
            }
        })
        .catch(error => {
            console.error('Fehler beim Hochladen:', error);
        });
    }
});
