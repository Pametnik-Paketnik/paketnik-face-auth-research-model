import tensorflow as tf
import mediapipe as mp
import cv2
import numpy as np
import sys
import os

print("----- Preverjanje namestitev knjižnic -----")

# 1. Preveri verzijo Pythona
print(f"Verzija Pythona: {sys.version.split(' ')[0]}")

# 2. Preveri TensorFlow in GPU
try:
    print(f"\nTensorFlow Verzija: {tf.__version__}")
    # Preveri razpoložljive fizične naprave (GPU)
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        print(f"Število GPU-jev, ki jih zazna TensorFlow: {len(gpus)}")
        for gpu in gpus:
            print(f"  - Ime GPU: {gpu.name}")
            # Neobvezno: Omogoči rast pomnilnika za GPU, preprečuje alociranje celotnega pomnilnika naenkrat
            tf.config.experimental.set_memory_growth(gpu, True)
    else:
        print("TensorFlow ni zaznal GPU-jev (Na VPS-u brez GPU je to pričakovano, na M4 Macu pa bi moral zaznati).")
    # Preveri, ali lahko TensorFlow izvede enostavno operacijo
    tf.constant([1.0, 2.0, 3.0]) + tf.constant([4.0, 5.0, 6.0])
    print("TensorFlow deluje pravilno.")
except Exception as e:
    print(f"NAPAKA pri preverjanju TensorFlow: {e}")
    print("Prepričaj se, da sta TensorFlow in tensorflow-metal pravilno nameščena za tvoj M4 čip.")

# 3. Preveri MediaPipe
try:
    print(f"\nMediaPipe Verzija: {mp.__version__}")
    # Inicializiraj rešitev MediaPipe (npr. zaznavanje obraza) za testiranje
    # To preveri, ali se vsi notranji moduli pravilno naložijo
    with mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
        print("MediaPipe Face Detection uspešno inicializiran!")
        # Poskusi obdelati prazno sliko (ne bo našel obraza, preveri pa delovanje celotnega cevovoda)
        dummy_image = np.zeros((480, 640, 3), dtype=np.uint8) # Črna slika
        # MediaPipe pričakuje RGB sliko
        dummy_image_rgb = cv2.cvtColor(dummy_image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(dummy_image_rgb)
        if results.detections: # To bi bilo None, če ni obrazov, ampak sam klic preveri cevovod
            print("MediaPipe obdelal prazno sliko (najdeni so bili obrazi, kar je morda nenavadno za prazno sliko).")
        else:
            print("MediaPipe obdelal prazno sliko (ni najdenih obrazov, kar je pričakovano).")

except Exception as e:
    print(f"NAPAKA pri preverjanju MediaPipe: {e}")
    print("Prepričaj se, da so sistemske odvisnosti za `opencv-python` pravilno nameščene (npr. preko Homebrewa).")

# 4. Preveri OpenCV
try:
    print(f"\nOpenCV Verzija: {cv2.__version__}")
    # Preprosta operacija OpenCV (npr. ustvarjanje prazne slike)
    blank_img_cv = np.zeros((100, 100, 3), dtype=np.uint8)
    print(f"OpenCV lahko ustvari sliko oblike: {blank_img_cv.shape}")
except Exception as e:
    print(f"NAPAKA pri preverjanju OpenCV: {e}")

# 5. Preveri NumPy
try:
    print(f"\nNumPy Verzija: {np.__version__}")
    dummy_array_np = np.array([1, 2, 3])
    print(f"NumPy lahko ustvari polje: {dummy_array_np}")
except Exception as e:
    print(f"NAPAKA pri preverjanju NumPy: {e}")


print("\n----- Preverjanje namestitve zaključeno -----")
print("Če se ni pojavilo nobeno sporočilo 'NAPAKA pri preverjanju', so tvoje ključne knjižnice verjetno pravilno nastavljene!")

# Namig za odpravljanje napak
print("\nNamig: Če imaš težave z namestitvijo, preveri naslednje:")
print("  1. Ali si aktiviral pravilno pyenv virtualno okolje?")
print("  2. Ali so Xcode Command Line Tools nameščeni: 'xcode-select --install'")
print("  3. Ali sta CMake in Boost nameščena preko Homebrew-a: 'brew install cmake boost'")
print("  4. Poskusi s 'pip cache purge' in nato ponovno namesti.")
