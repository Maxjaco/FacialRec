import time

import cv2
import face_recognition
from Facial_rec.Facial_rec import FacialRec

print("Load in video")
video_capture = cv2.VideoCapture("rec_movie.h264")
length = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

frames = []
frame_count = 0
print("start loop")
while video_capture.isOpened():
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Bail out when the video file ends
    if not ret:
        print("video ended at frame: " + str(len(frames)))
        break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    frame = frame[:, :, ::-1]

    # Save each frame of the video to a list
    frame_count += 1
    frames.append(frame)

    # Every 128 frames (the default batch size), batch process the list of frames to find faces
    if len(frames) == 280:
        millis = int(round(time.time() * 1000))
        FacialRec().facial_rec(frames)
        millis1 = int(round(time.time() * 1000))
        print(millis1 - millis)

        frames = []

