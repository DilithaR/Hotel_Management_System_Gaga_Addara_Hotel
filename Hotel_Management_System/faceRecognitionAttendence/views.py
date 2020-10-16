from django.shortcuts import render
import face_recognition
from cv2 import cv2
from PIL import Image

# Create your views here.
cam = cv2.VideoCapture(0)
s , img = cam.read()
if s:
    faceImg_1 = face_recognition.load_image_file("/media/auction.jpg")
    faceImg_1_encode = face_recognition.face_encodings(faceImg_1)[0]

    camFrame = cv2.resize(
        img,
        (0 , 0),
        fx = 0.25,
        fy = 0.25,
    )

    rgb_CamFrame = camFrame[: , : , ::-1]

    face_Location = face_recognition.face_locations(rgb_CamFrame)
    face_Encordings = face_recognition.face_encodings(rgb_CamFrame , face_Location)

    match = face_recognition.compare_faces(faceImg_1_encode , face_Encordings)

    top , right , bottom , left = (face_recognition.face_locations(img))[0]

    print("Found face at top:{} , right{} , bottom{} , left{}")
    cam_Image = img[top:bottom , left:right]
    pil_Image = Image.fromarray(cam_Image)
    pil_Image.save()

    print(match)
    if match[0]:
        print("Images Are matched")
    else:
        print("Images are not matching")





