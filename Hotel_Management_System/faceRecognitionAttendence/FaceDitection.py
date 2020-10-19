from django.shortcuts import render
import os
import face_recognition
from cv2 import cv2
from PIL import Image
from asgiref.sync import async_to_sync , sync_to_async
from django.conf import settings

fd_WebCam = cv2.CascadeClassifier(os.path.join(
    settings.BASE_DIR, 'opencv_haarcascade_data/haarcascade_frontalface_default.xml'))

def compareImages(empImage, request , emp):
    cam = cv2.VideoCapture(0)


    s, img = cam.read()

    if s:

        cv2.namedWindow("cam-test")
        cv2.imshow("cam-test", img)
        # cv2.waitKey(0)
        cv2.destroyWindow("cam-test")
        cv2.imwrite("filename.jpg", img)

        faceImg_1 = face_recognition.load_image_file("media/" + str(empImage))
        faceImg_1_encode = face_recognition.face_encodings(faceImg_1)[0]

        grayImg = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

        camFrame = cv2.resize(
            img,
            (0, 0),
            fx=0.25,
            fy=0.25
        )

        detFaces = fd_WebCam.detectMultiScale(
            grayImg,
            scaleFactor = 1.3,
            minNeighbors= 3,
            minSize=(30 , 30)

        )

        print("Found {0} Faces!".format(len(detFaces)))

        rgb_CamFrame = camFrame[:, :, ::-1]

        face_Location = face_recognition.face_locations(rgb_CamFrame)
        face_Encordings = face_recognition.face_encodings(
            rgb_CamFrame, face_Location)

        if len(detFaces) == 1:
            match = face_recognition.compare_faces(faceImg_1_encode, face_Encordings)
            print("match is" + str(match))

            if match[0]:
                print("Images Are matched")
            else:
                print("Images are not matching")
        else:
            match = "False"

        # top, right, bottom, left = (face_recognition.face_locations(img))[0]

        # print("Found face at top:{} , right{} , bottom{} , left{}")
        # cam_Image = img[top:bottom, left:right]
        # pil_Image = Image.fromarray(cam_Image)
        # pil_Image.save()
    return match[0]
