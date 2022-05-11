import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, DetectedFace

from apps.models import FaceInfo

from dotenv import load_dotenv
load_dotenv()

KEY = os.getenv('KEY')
KEY2 = os.getenv('KEY2')
ENDPOINT = os.getenv('ENDPOINT')

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

# Detect a face in an image that contains a single face
single_face_image_url = 'https://www.biography.com/.image/t_share/MTQ1MzAyNzYzOTgxNTE0NTEz/john-f-kennedy---mini-biography.jpg'


single_image_name = os.path.basename(single_face_image_url)
# We use detection model 3 to get better performance.
detected_faces = face_client.face.detect_with_url(url=single_face_image_url, detection_model='detection_03')
if not detected_faces:
    raise Exception('No face detected from image {}'.format(single_image_name))

# Display the detected face ID in the first single-face image.
# Face IDs are used for comparison to faces (their IDs) detected in other images.
print('Detected face ID from', single_image_name, ':')
for face in detected_faces: print (face.face_id)
print()

# Save this ID for use in Find Similar
first_image_face_ID = detected_faces[0].face_id

single_face_image_url = 'https://farm3.static.flickr.com/2496/3800942346_90c2ce1d54.jpg'
#single_face_image_url = 'https://img.cinematoday.jp/a/RBj7QU9ad-uB/_size_640x/_v_1629858458/main.jpg'
#single_face_image_url = 'https://app.box.com/s/1ago5ti67baf27qfwfzlhmcpgtvzrkl8'

# Attributes you want returned with the API call, a list of FaceAttributeType enum (string format)
face_attributes = ['age', 'gender', 'headPose', 'smile', 'facialHair', 'glasses', 'emotion']

# -----
# Detect a face in an image that contains a single face
#single_face_image_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
single_image_name = os.path.basename(single_face_image_url)
# We use detection model 3 to get better performance.
#detected_faces = face_client.face.detect_with_url(url=single_face_image_url, detection_model='detection_03')

def getFaceSample(filePath):
#    detected_faces = face_client.face.detect_with_url(url=imgData, return_face_landmarks=True, return_face_attributes=face_attributes)
    print('Path:')
    print(filePath)
    imgData = open(filePath, 'rb')
    

    detected_faces = face_client.face.detect_with_stream(image=imgData, return_face_attributes=face_attributes)
#    detected_faces = face_client.face.detect_with_url(url=single_face_image_url, return_face_attributes=face_attributes)
    if not detected_faces:
        raise Exception('No face detected from image {}'.format(single_image_name))


    for face in detected_faces:
        print()
        print('Detected face ID from', os.path.basename(single_face_image_url), ':')
        # ID of detected face
        print(face.face_id)
        # Show all facial attributes from the results
        print()
        print('Facial attributes detected:')
        print('Age: ', face.face_attributes.age)
        print('Gender: ', face.face_attributes.gender)
        print('Head pose: ', face.face_attributes.head_pose)
        print('Smile: ', face.face_attributes.smile)
        print('Facial hair: ', face.face_attributes.facial_hair)
        print('Glasses: ', face.face_attributes.glasses)
        print('Emotion: ')
        print('\tAnger: ', face.face_attributes.emotion.anger)
        print('\tContempt: ', face.face_attributes.emotion.contempt)
        print('\tDisgust: ', face.face_attributes.emotion.disgust)
        print('\tFear: ', face.face_attributes.emotion.fear)
        print('\tHappiness: ', face.face_attributes.emotion.happiness)
        print('\tNeutral: ', face.face_attributes.emotion.neutral)
        print('\tSadness: ', face.face_attributes.emotion.sadness)
        print('\tSurprise: ', face.face_attributes.emotion.surprise)
        print()
    
#    imgData =  drawImg(imgData)   
#    faceInfo = FaceInfo(
      #detected_faces = detected_faces,
#      faceImg = imgData,
#    )           
        
    return detected_faces
#    return faceInfo

# Convert width height to a point in a rectangle
def getRectangle(faceDictionary):
    rect = faceDictionary.face_rectangle
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height

    return ((left, top), (right, bottom))

def drawFaceRectangles() :
    # Download the image from the url
    response = requests.get(single_face_image_url)
    img = Image.open(io.BytesIO(response.content))

    # For each face returned use the face rectangle and draw a red box.
    print('Drawing rectangle around face... see popup for results.')
    draw = ImageDraw.Draw(img)
    for face in detected_faces:
        draw.rectangle(getRectangle(face), outline='red')

    # Display the image in the default image browser.
    # img.show()
    
    return img

def drawImg(imgData):
    draw = ImageDraw.Draw(imgData)
    for face in detected_faces:
        draw.rectangle(getRectangle(face), outline='red')

    # Display the image in the default image browser.
    # img.show()
    
    return imgData
    

