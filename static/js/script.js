document.addEventListener('DOMContentLoaded', function() {
    const uploadButton = document.getElementById('uploadButton');
    const fileInput = document.getElementById('fileInput');

    // Wenn der Button geklickt wird, öffne das Eingabefeld für die Datei
    uploadButton.addEventListener('click', function(event) {
        event.preventDefault(); // Verhindert, dass das Formular sofort abgeschickt wird
        fileInput.click(); // Öffnet den Datei-Explorer, um eine Datei auszuwählen
    });

    // Wenn eine Datei ausgewählt wird
    fileInput.addEventListener('change', function(event) {
        if (fileInput.files.length === 0) {
            alert('Bitte wählen Sie eine Datei aus.'); // Warnung anzeigen, wenn keine Datei ausgewählt ist
            return; // Stoppt die Ausführung, wenn keine Datei ausgewählt wurde
        }

        const formData = new FormData();
        formData.append('image', fileInput.files[0]); // Fügt die ausgewählte Datei hinzu

        // Bildanalyse sofort nach der Auswahl durchführen
        fetch('/upload', {
            method: 'POST',
            body: formData // Sendet die Daten an den Server
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(`Fehler: ${data.error}`); // Fehlerbehandlung
            } else {
                // Ergebnisse anzeigen
                document.getElementById('result').style.display = 'block'; // Zeigt den Ergebnisbereich
                document.getElementById('uploadedImage').src = data.image_url; // Bild anzeigen
                document.getElementById('resultText').textContent = data.result; // Ergebnis anzeigen
            }
        })
        .catch(error => {
            console.error('Fehler beim Hochladen:', error);
        });
    });
});
