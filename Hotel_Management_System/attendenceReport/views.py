from django.shortcuts import render
from datetime import date, datetime , timedelta
from userlogin.models import Employee, Admin
from faceRecognitionAttendence.models import Attendencesheet
from attendenceReport.supportClasses import EmpToday , EmpFull
import json
import math
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse


def attendenceReport (request):

    cDate = date.today()
    current_date = cDate.strftime("%Y-%m-%d")

    attendees = Attendencesheet.objects.filter(date=current_date)
    attendees = attendees.filter(status="Available")

    availEmp = []

    for emp in attendees:
         print(emp.date)
         fullEmp = Employee.objects.get(empid=emp.empid)
         availEmp.append(fullEmp)

    now = datetime.now()
    monday = now - timedelta(days= now.weekday())
    sunday = monday + timedelta(days = 6)
    mDate =monday.date()
    sDate = sunday.date()
    print("sunday Date" + str(sDate))

    # for one_date in range(mDate, sDate):
    #     print(one_date)

    empCountList = []

    empCountToday = Attendencesheet.objects.filter(date=current_date).count()

    while mDate <= sDate:
        empCount = Attendencesheet.objects.filter(date=mDate).count()
        empCountList.append(empCount)
        mDate = mDate + timedelta(days = 1)
        

    #getting employee full report

    fullAttendees = Attendencesheet.objects.filter(date=current_date)

    fullAttendList = []

    for emp in fullAttendees:
        empEnrty = Employee.objects.get(empid=emp.empid)
        empFullName = empEnrty.f_name + " " + empEnrty.l_name
        fullEmp = EmpToday(empFullName , emp.empid , emp.date , emp.timein , "N/A")
        fullAttendList.append(fullEmp)

    day_of_month = now.day

    expected_Days = math.floor(day_of_month * 0.80)

    print("day_of_month : " + str(day_of_month))
    print("expected_Days : " + str(expected_Days))

    fullRepList = []

    totEmps = Employee.objects.all()
    for emp in totEmps:
        empCount = Attendencesheet.objects.filter(empid=emp.empid).count()        
        empFullName = emp.f_name + " " + emp.l_name
        print(empFullName + " : " + str(empCount))
        leaves = expected_Days - empCount
        fullRep = EmpFull(empFullName, emp.empid,
                          expected_Days, empCount, leaves)
        fullRepList.append(fullRep)

    context = {'mon': json.dumps(empCountList[0]), 'tue': json.dumps(empCountList[1]), 'wed': json.dumps(empCountList[2]), 'thu': json.dumps(empCountList[3]), 'fri': json.dumps(empCountList[4]), 'sat': json.dumps(empCountList[5]), 'sun': json.dumps(empCountList[6]), 'AvailableEmp': availEmp, 'dailyAttendence': empCountList,
               'TodayCount': empCountToday, 'fullAttendList': fullAttendList, 'FullReportVals': fullRepList ,'Title' : "ATTENDANCE REPORT"}

    return render(request, "AttendenceReport.html", context)

#Pdf generation function
def generatePDf(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    cDate = date.today()
    current_date = cDate.strftime("%Y-%m-%d")
    day_of_month = now.day

    expected_Days = math.floor(day_of_month * 0.80)


    fullRepList = []

    totEmps = Employee.objects.all()
    for emp in totEmps:
        empCount = Attendencesheet.objects.filter(empid=emp.empid).count()
        empFullName = emp.f_name + " " + emp.l_name
        print(empFullName + " : " + str(empCount))
        leaves = expected_Days - empCount
        fullRep = EmpFull(empFullName, emp.empid,
                          expected_Days, empCount, leaves)
        fullRepList.append(fullRep)

    context = {'FullReportVals': fullRepList,
               'currentDate': current_date, 'currentTime': current_time}

    template = get_template("monthlyReportPDF.html")
    report = template.render(context)
    response = BytesIO()

    pdfReport = pisa.pisaDocument(BytesIO(report.encode("UTF-8")) , response)

    if not pdfReport.err:
        return HttpResponse(response.getvalue() , content_type = "application/pdf")
    else:
        return HttpResponse("Error In Generating pdf")


    return render(request, "monthlyReportPDF.html", context)
