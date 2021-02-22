import pickle
import time

import face_recognition
import cv2
import numpy as np
import re
import heapq
import uuid






class FacialRec:
    def __init__(self):
        pass

    def facial_rec(self, images_list):
        known_face_names, known_face_encodings = self.load_encodings()
        pepole_entered = {}
        max_faces = 0
        batch_of_face_locations = []
        print("Doing batch work")
        millis = int(round(time.time() * 1000))
        for image in images_list:
            batch_of_face_locations.append(face_recognition.face_locations(image, number_of_times_to_upsample=1, model='cnn'))

        millis1 = int(round(time.time() * 1000))
        print("Batchwork took: " + str(millis1-millis))
        millis_all = int(round(time.time() * 1000))

        for frame_number_in_batch, face_locations in enumerate(batch_of_face_locations):
            if len(face_locations) > 0:

                unknown_face_encodings = face_recognition.face_encodings(images_list[frame_number_in_batch], known_face_locations=face_locations)
                # Loop through each face in this frame of video
                for (top, right, bottom, left), face_encoding in zip(face_locations, unknown_face_encodings):
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.50)

                    name = "Unknown"

                    # If a match was found in known_face_encodings, just use the first one.

                    if True in matches:
                        first_match_index = matches.index(True)
                        name = "_".join(re.findall("[a-zA-Z]+", known_face_names[first_match_index]))
                        if name in pepole_entered:
                            pepole_entered[name] += 1
                        else:
                            pepole_entered[name] = 1
                    else:
                        if name in pepole_entered:
                            pepole_entered[name] += 1
                        else:
                            pepole_entered[name] = 1


                if max_faces < len(face_locations):
                    max_faces = len(face_locations)

        found_faces = heapq.nlargest(max_faces, pepole_entered, key=pepole_entered.get)
        print(found_faces)
        print(pepole_entered)
        millis_all_end = int(round(time.time() * 1000))

        print("To find all faces: " + str(millis_all_end-millis_all))



    def load_encodings(self):
        with open('dataset_face_encodings.dat', 'rb') as f:
            all_face_encodings = pickle.load(f)

        # Grab the list of names and the list of encodings
        face_names = list(all_face_encodings.keys())
        known_face_encodings = np.array(list(all_face_encodings.values()))

        return face_names, known_face_encodings