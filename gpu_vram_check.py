import os

import face_recognition

path = "/home/dev/GIT/facial_be/pictures"

for root, dir, files in os.walk(path):
    for file in files:
        images = []
        for i in range(20):
            images.append(face_recognition.load_image_file(path + "/" + file))
        print("Starting facelocation for" + str(file))
        for image in images:
            face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=1, model="cnn")


