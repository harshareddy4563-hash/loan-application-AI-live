import face_recognition
import numpy as np

def get_face_encoding(image_bytes):
    image = face_recognition.load_image_file(image_bytes)
    enc = face_recognition.face_encodings(image)
    if len(enc) != 1:
        return None
    return enc[0]

def verify_faces(enc1, enc2):
    dist = np.linalg.norm(enc1 - enc2)
    return dist > 0.6
