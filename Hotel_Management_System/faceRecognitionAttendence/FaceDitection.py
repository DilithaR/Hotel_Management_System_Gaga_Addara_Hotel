from django.shortcuts import render
import os
import face_recognition
from cv2 import cv2
from PIL import Image


def compareImages():
    cam = cv2.VideoCapture(0)


    s, img = cam.read()

    if s:

        cv2.namedWindow("cam-test")
        cv2.imshow("cam-test", img)
        # cv2.waitKey(0)
        cv2.destroyWindow("cam-test")
        cv2.imwrite("filename.jpg", img)

        faceImg_1 = face_recognition.load_image_file("mahendra.jpg")
        faceImg_1_encode = face_recognition.face_encodings(faceImg_1)[0]

        camFrame = cv2.resize(
            img,
            (0, 0),
            fx=0.25,
            fy=0.25
        )

        rgb_CamFrame = camFrame[:, :, ::-1]

        face_Location = face_recognition.face_locations(rgb_CamFrame)
        face_Encordings = face_recognition.face_encodings(
            rgb_CamFrame, face_Location)

        match = face_recognition.compare_faces(faceImg_1_encode, face_Encordings)

        # top, right, bottom, left = (face_recognition.face_locations(img))[0]

        # print("Found face at top:{} , right{} , bottom{} , left{}")
        # cam_Image = img[top:bottom, left:right]
        # pil_Image = Image.fromarray(cam_Image)
        # pil_Image.save()

        print(match)
        if match[0]:
            print("Images Are matched")
        else:
            print("Images are not matching")
