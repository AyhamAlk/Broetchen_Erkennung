import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Setze Parameter
IMG_WIDTH, IMG_HEIGHT = 224, 224
NUM_CLASSES = 2  # Anzahl der Klassen
BATCH_SIZE = 32
EPOCHS = 10

# Simulierte Trainingsdaten erstellen
# Erstelle zufällige Bilder (z.B. 1000 Bilder) für zwei Klassen
X_train = np.random.rand(1000, IMG_WIDTH, IMG_HEIGHT, 3)  # 1000 Bilder
y_train = np.random.randint(0, NUM_CLASSES, 1000)  # 1000 Zufalls-Labels (0 oder 1)

# One-hot Encoding der Labels
y_train_one_hot = tf.keras.utils.to_categorical(y_train, num_classes=NUM_CLASSES)

# Daten-Generator für das Training
train_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow(X_train, y_train_one_hot, batch_size=BATCH_SIZE)

# Modell erstellen
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(NUM_CLASSES, activation='softmax')  # Aktivierungsfunktion für mehrere Klassen
])

# Kompiliere das Modell
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Modell trainieren
model.fit(train_generator, epochs=EPOCHS)  # Erhöhe die Anzahl der Epochen nach Bedarf

# Speichere das Modell
model.save('model.h5')
print("Dummy-Modell wurde erfolgreich gespeichert als 'model.h5'")
