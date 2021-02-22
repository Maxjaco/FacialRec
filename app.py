import base64
import time

from flask import Flask, request, Response, render_template
from Facial_rec.Facial_rec import FacialRec
import numpy as np
import cv2
import uuid

# Initialize the Flask application
app = Flask(__name__)

@app.route('/api/test', methods=['POST'])
def test():
    r = request
    images = []
    for k in r.json:
        decoded_img = base64.b64decode(r.json[k])
        nparr = np.fromstring(decoded_img, np.uint8)
        rgb_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        images.append(rgb_img)

    FacialRec().facial_rec(images)
    return Response(status=202)



# start flask app
if __name__ == '__main__':
    app.run(threaded=True, host="0.0.0.0", port=5000, debug=True)