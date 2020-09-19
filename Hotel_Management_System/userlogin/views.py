from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Admin, Employee
from django.core.files.storage import FileSystemStorage
from .models import generateRandomeNum
from django.shortcuts import redirect
from .forms import custmoneForm
from django.conf import settings
from datetime import datetime
import string
from secrets import choice

# Create your views here.


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def signUp(request):
    return render(request, 'Signup.html')


def admin(request):
    return render(request, 'Dashboard.html')


def forgetpassword(request):
    return render(request, 'Forgot_password_1.html')


def forgetpw2(request):
    forgetPwgetEmail = request.GET['forgetPwgetEmail']

    if Customer.objects.filter(email=forgetPwgetEmail).exists():
        secCode = ''.join(
            [choice(string.ascii_uppercase + string.digits) for _ in range(8)])
        request.session["securityCode"] = secCode
        request.session["UserEmail"] = forgetPwgetEmail
        print("Email exist : " + secCode)
        return render(request, 'Forgot_password_2.html')

    else:
        return render(request, 'Forgot_password_1.html')


def fogetPw3(request):
    submitSecCode = request.POST.get('submitSecCode', None)
    checkSession = request.session['securityCode']
    print("Recieved session is : " + checkSession)
    print("Typed sec code : " + submitSecCode)
    if checkSession == submitSecCode:
        print("Security Codes matched")
        del request.session['securityCode']
        return render(request, 'Forgot_password_3.html')
    else:
        request.session.flush()
        return render(request, 'Forgot_password_1.html')


def resetPWinForgetPw(request):
    leagalCusEmail = request.session['UserEmail']
    leagalCus = Customer.objects.get(email=leagalCusEmail)

    password = request.POST['resetPw']
    confPassword = request.POST['resetConfPw']

    if password == confPassword:
        leagalCus.password = password
        leagalCus.save()
        return render(request, 'login.html')
    else:
        return render(request, 'Forgot_password_3.html')


def customerLogout(request):
    request.session.flush()
    return render(request, 'login.html')


def addEmployees(request):
    return render(request, 'AddEmployee.html')


def employeerepo(request):
    return render(request, 'AttendenceReport.html')


def employeeList(request):
    emp = Employee.objects.all()
    return render(request, 'EmployeeList.html',  {'employees': emp})


def myprofile(request):
    print("sesseionvalue : " + request.session['userid'])
    cus1 = Customer.objects.get(cusid=request.session['userid'])
    return render(request, 'User_profile.html', {'customer': cus1})


# login function
def vertifyLogin(request):

    Email = request.POST['loginEmail']
    Password = request.POST['loginPw']

    print(Password)

    cusExist = Customer.objects.filter(email=Email).exists()

    if cusExist == True:
        #auth.login(request, customer)
        customer = Customer.objects.get(email=Email)
        if customer.password == Password:
            request.session['userid'] = customer.cusid
            print("Customer valid")
            return render(request, 'index.html', {'userid': customer.cusid, 'userEmail': customer.email})
        else:
            request.session['userid'] = None
            return redirect('login')
    else:
        adminExist = Admin.objects.filter(adminid=Email).exists()
        if adminExist == True:
            admin = Admin.objects.get(adminid=Email)
            if admin.password == Password:
                request.session['eid'] = admin.adminid
                print("admin valid")
                return render(request, 'Dashboard.html')
            else:
                request.session['userid'] = None
                return redirect('login')

    #     admin = auth.authenticate(adminid=Email, password = Password)
    #     print("add checked")
    #     if admin is not None:
    #     auth.login(request, admin)

    # print("function skiped")
    # return render(request, 'login.html')

# Signup function


def signUpVer(request):

    rand = generateRandomeNum()

    custId = "CUS" + rand.fiveNums()
    print("custId" + custId)
    Email = request.POST['signEmail']
    Password = request.POST['signPW']
    ConPw = request.POST['signConfermPw']
    fname = request.POST['signFname']
    lname = request.POST['signLname']

    if ConPw != Password:
        return render(request, 'login.html')

    # elif Customer.objects.filter(email=Email).exists:
    #     return render(request, 'login.html')

    # elif Customer.objects.filter(cusid=custId).exists:
    #     return render(request, 'login.html')

    else:
        customer = Customer(cusid=custId, email=Email,
                            password=Password, f_name=fname, l_name=lname)
        customer.save()
        print("Saved Customer")
        return render(request, 'index.html')


def updateCus(request, id_cus):

    cus = Customer.objects.get(cus_index=id_cus)
    print(id_cus)
    cus.email = request.POST['Edit_Email']
    cus.cusnic = request.POST['Edit_Nic']
    cus.address_l1 = request.POST['AddressLineOne']
    cus.address_l2 = request.POST['Edit_AddLine2']
    cus.postcode = request.POST['Edit_PCode']
    cus.f_name = request.POST['Edit_Fname']
    cus.l_name = request.POST['Edit_Lname']
    uploaded_File = request.FILES['cusImg']
    cus.img = uploaded_File.name
    print(uploaded_File.name)
    print(uploaded_File.size)
    fs = FileSystemStorage()
    fs.save(uploaded_File.name, uploaded_File)

    cus.save()
    cus = Customer.objects.get(cusid=request.session['userid'])
    return render(request, 'User_profile.html', {'customer': cus, 'media_url': settings.MEDIA_URL})


def adduser(request):

    rand = generateRandomeNum()

    addEmpEID = "EMP" + rand.fiveNums()
    addEmpFname = request.POST['addEmpFname']
    addEmpLname = request.POST['addEmpLname']
    addEmpNIC = request.POST['addEmpNIC']
    addEmpGender = request.POST['addEmpGender']
    addEmpEmail = request.POST['addEmpEmail']
    addEmpsetOccu = request.POST['setOccu']
    addEmpPhone = request.POST['addEmpPhone']
    addEpLineOne = request.POST['addEpLineOne']
    addEpLineTwo = request.POST['addEpLineTwo']
    addEmpcity = request.POST['addEmpcity']
    addEmpPCode = request.POST['addEmpPCode']
    addempDateOfJoin = request.POST.get(
        'dateOfJoin', datetime.today().strftime('%Y-%m-%d'))
    addempSal = request.POST['addempSal']
    addempOTRate = request.POST['addempOTRate']
    addEmpImg = request.FILES['empImgUpload']

    cusImg = addEmpImg.name
    cussize = addEmpImg.size

    filesys = FileSystemStorage()
    filesys.save(addEmpImg.name, addEmpImg)

    print(cusImg)

    employee = Employee(empid=addEmpEID, f_name=addEmpFname,
                        l_name=addEmpLname, empnic=addEmpNIC, gender=addEmpGender,    email=addEmpEmail, phone=addEmpPhone,
                        address_l1=addEpLineOne, address_l2=addEpLineTwo, postcode=addEmpPCode, reg_date=addempDateOfJoin, basic_sal=addempSal,
                        ot_rate=addempOTRate, occu=addEmpsetOccu, img=cusImg)
    employee.save()
    print("Saved Customer")
    emp = Employee.objects.all()
    return render(request, 'EmployeeList.html', {'employees': emp})


def fullemployee(request, id_emp):
    emp = Employee.objects.get(emp_index=id_emp)
    return render(request, 'ViewEmployee.html', {'employee': emp})


def editemp(request):

    #eid = request.GET['Edit_eid']
    addEmpFname = request.GET['Edit_E_Fname']
    addEmpLname = request.GET['Edit_E_Lname']
    addEmpNIC = request.GET['Edit_E_nic']
    #addEmpMale = request.GET['addEmpMale']
    addEmpEmail = request.GET['Edit_E_email']

    addEmpPhone = request.GET['Edit_E_phone']
    addEpLineOne = request.GET['Edit_E_assL1']
    addEpLineTwo = request.GET['Edit_E_assL2']
    addEmpcity = request.GET['Edit_E_city']
    addEmpPCode = request.GET['Edit_Epost_code']
    #addempDateOfJoin = request.GET['Edit_Appdate']
    addempSal = request.GET['Edit_Bsal']
    addempOTRate = request.GET['Edit_OTrate']

    employee = Employee(empid='EMP98245', f_name=addEmpFname,
                        l_name=addEmpLname, empnic=addEmpNIC, gender='Male',    email=addEmpEmail, phone=addEmpPhone,
                        address_l1=addEpLineOne, address_l2=addEpLineTwo, postcode=addEmpPCode, basic_sal=addempSal,
                        ot_rate=addempOTRate)

    return render(request, 'ViewEmployee.html', {'employee': employee})


def filterEmployees(request):
    srchByEid = request.GET.get('srchByEid', None)
    srchByName = request.GET.get('srchByName', None)
    srchByLName = request.GET.get('srchByLName', None)
    srchByOccu = request.GET.get('srchByOccu', None)
    srchByGender = request.GET.get('srchByGender', None)
    srchBySal = request.GET.get('srchBySal', None)

    queryArray = {}

    if(srchByEid != ""):
        queryArray['empid'] = srchByEid.strip()
    if(srchByName != ""):
        queryArray['f_name'] = srchByName.strip()
    if(srchByLName != ""):
        queryArray['l_name'] = srchByLName.strip()
    if(srchByGender != None):
        queryArray['gender'] = srchByGender.strip()
    if(srchBySal != ""):
        queryArray['basic_sal'] = srchBySal.strip()
    if(srchByOccu != None):
        queryArray['occu'] = srchByOccu.strip()

    # print(**queryArray)

    # query = []
    # if(srchByEid != ""):
    #     query = query + "empid = " + srchByEid.strip() + " ,"
    # if(srchByName != ""):
    #     query = query + "f_name = " + srchByName.strip() + " ,"
    # if(srchByGender != None):
    #     query = query + "gender = " + srchByGender.strip() + " ,"
    # if(srchBySal != ""):
    #     query = query + "basic_sal = " + srchBySal.strip()

    # print(query)

    filteedSet = Employee.objects.filter(**queryArray)

    print("filtered data : ")
    print(filteedSet)
    print("filtered data end")

    print("Recieved Details : Salary -" + srchBySal,
          srchByName, srchByGender, srchByEid, srchByOccu)

    # return employeeList(request)
    return render(request, 'EmployeeList.html',  {'employees': filteedSet})
