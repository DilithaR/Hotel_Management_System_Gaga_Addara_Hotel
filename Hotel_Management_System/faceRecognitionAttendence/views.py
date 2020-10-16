from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
from faceRecognitionAttendence.Webcam import MyWebCam
from faceRecognitionAttendence.FaceDitection import compareImages


def employeeAttendence(request):
    return render(request, 'EmployeeAttendence.html')


def startCam(Webcam):
    while True:
        frame = Webcam.get_video()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def connectCamera(request):
    return StreamingHttpResponse(startCam(MyWebCam()), content_type = 'multipart/x-mixed-replace; boundary=frame')


def validateEmp(request):
    print("Validate Emp Executed")
    compareImages()
    return render(request, 'EmployeeAttendence.html')

