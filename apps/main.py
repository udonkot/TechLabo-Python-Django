import base64
import io
import os
import requests
import imghdr
from PIL import Image, ImageDraw, ImageFont
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
# from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, DetectedFace

from dotenv import load_dotenv
load_dotenv()

# 環境変数取得
KEY = os.getenv('KEY')
KEY2 = os.getenv('KEY2')
ENDPOINT = os.getenv('ENDPOINT')

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

"""
FaceAPI サンプル実装
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
"""

# サンプル画像
single_face_image_url = 'https://farm3.static.flickr.com/2496/3800942346_90c2ce1d54.jpg'
#single_face_image_url = 'https://img.cinematoday.jp/a/RBj7QU9ad-uB/_size_640x/_v_1629858458/main.jpg'
#single_face_image_url = 'https://app.box.com/s/1ago5ti67baf27qfwfzlhmcpgtvzrkl8'

# Attributes you want returned with the API call, a list of FaceAttributeType enum (string format)
# FaceAPIの返却する項目(全項目)
face_attributes = ['age', 'gender', 'headPose', 'smile', 'facialHair', 'glasses', 'emotion', 'hair', 'makeup', 'occlusion', 'accessories', ]

def getFaceSample(filePath):
    """ 顔情報取得
    
    画像から検出した顔情報を返却する。

    """    

#    detected_faces = face_client.face.detect_with_url(url=imgData, return_face_landmarks=True, return_face_attributes=face_attributes)
    # アップロードファイル取得
    # print('Path:')
    # print(filePath)
    imgData = open(filePath, 'rb')

    retArray = []
    
    
    # 顔識別情報取得
    detected_faces = face_client.face.detect_with_stream(image=imgData, return_face_attributes=face_attributes)
    # ファイルパスを指定する場合はこちら
    # detected_faces = face_client.face.detect_with_url(url=single_face_image_url, return_face_attributes=face_attributes)
    
    # 画像から顔情報が検出できない場合は終了
    if not detected_faces:
        return retArray
#        raise Exception('No face detected from image {}'.format(filePath))
    
    # 取得結果解析
    for face in detected_faces:
        # Debug用ログ出力
        # showFaceLog(face)
        faceImgData = Image.open(filePath)
        drawing = ImageDraw.Draw(faceImgData)

        # 検出した顔に枠線追加
        drawing.rectangle(getRectangle(face), outline='Red', width = 3)
        
        # 枠線を追加した画像を返却するようセット
        output = io.BytesIO()
        image_type = imghdr.what(filePath)
        # print('imgType : ' + image_type)
        faceImgData.save(output, format=image_type)
        wrkArray = [face, base64.b64encode(output.getvalue()).decode("ascii")]
        retArray.append(wrkArray)
    
#    faceImgData = Image.open(filePath)
#    drawing = ImageDraw.Draw(faceImgData)
#    for face in detected_faces:
#      drawing.rectangle(getRectangle(face), outline='Red', width = 3)
#    faceImgData.show()
        
    return retArray
#    return faceInfo

# Convert width height to a point in a rectangle
def getRectangle(faceDictionary):
    """ 顔座標取得
    
    画像から検出した顔の座標を返却する。

    """    
    rect = faceDictionary.face_rectangle
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height

    return ((left, top), (right, bottom))

def showFaceLog(face):
    """ Face Attributeコンソール出力
    
    取得したFaceオブジェクトの情報をprintで出力する

    """    

    print()
    # print('Detected face ID from', os.path.basename(single_face_image_url), ':')
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
