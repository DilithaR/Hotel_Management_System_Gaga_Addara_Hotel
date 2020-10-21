from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
from faceRecognitionAttendence.Webcam import MyWebCam
from faceRecognitionAttendence.FaceDitection import compareImages
from userlogin.models import Employee , Admin
from datetime import date , datetime
from .models import Attendencesheet


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
    empID = request.POST['empID_check']
    empExist = Employee.objects.filter(empid=empID).exists()

    if empExist == True:
        emp = Employee.objects.get(empid=empID)
        print(emp.img)
        empImg = emp.img
        print(empImg)
        #result = compareImages("mahendra.jpg")
        result = compareImages("mahendra.jpg" , request , emp)
        print(result)

        if result == True:
            print("Inside if statement")
            cTime = datetime.now()
            current_time = cTime.strftime("%H:%M:%S")
            cDate = date.today()
            current_date = cDate.strftime("%Y-%m-%d")
            return render(request, 'EmployeeAttendence.html', {'Employee': emp, 'time': current_time, 'date': current_date})
        else:
            print("result is false")
            return render(request, 'EmployeeAttendence.html')
    else:
        print("emp Not Found")
        return render(request, 'EmployeeAttendence.html')
    

def markAttendence(request):
    
    empID = request.POST['hiddenID']
    today = request.POST['today']
    inTime = request.POST['inTime']

    print(empID , inTime , today)

    attendEmp = Attendencesheet(
        empid=empID, date=today, timein=inTime, status="Available")
    attendEmp.save()

    return render(request, 'EmployeeAttendence.html' , {'marked': True})
