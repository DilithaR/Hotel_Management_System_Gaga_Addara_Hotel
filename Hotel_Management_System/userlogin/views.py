from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer , Admin , Employee
from .models import generateRandomeNum
from django.contrib.auth.models import auth
from django.shortcuts import redirect
from .forms import custmoneForm

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
    return render(request, 'Forgot_password_2.html')


def fogetPw3(request):
    return render(request, 'Forgot_password_3.html')


def customerLogout(request):
    return render(request, 'login.html')


def addEmployees(request):
    return render(request, 'AddEmployee.html')


def employeerepo(request):
    return render(request, 'AttendenceReport.html')

    


def myprofile(request):
    print("sesseionvalue : " + request.session['userid'])
    cus1 = Customer.objects.get(cusid=request.session['userid'])
    return render(request, 'User_profile.html' , {'customer' : cus1} )

# login function
def vertifyLogin(request):
    
    Email = request.POST['loginEmail']
    Password = request.POST['loginPw']

    print(Password)

    # admin = Admin.objects.get(adminid=Email)
    # if admin is not None:
    #     #auth.login(request, customer)
    #     if admin.password == Password:
    #         request.session['userid'] = admin.adminid
    #         print("Customer valid")
    #         return render(request, 'Dashboard.html', {'userid': admin.adminid})
    #     else:
    #         request.session['userid'] = None
    #         return render(request, 'Dashboard.html')
    # else:
    #     customer = Customer.objects.get(email=Email)
    #     if customer is not None:
    #         if customer.password == Password:
    #             request.session['eid'] = customer.adminid
    #             print("customer valid")
    #             return render(request, 'index.html', {'userid': customer.cusid, 'userEmail': customer.email})
    #     else:
    #         request.session['userid'] = None
    #         return redirect('login')



    #-----------------------------------------------

    
    customer = Customer.objects.get(email=Email)


    if customer is not None:
        #auth.login(request, customer)
        if customer.password == Password:
            request.session['userid'] = customer.cusid
            print("Customer valid")
            return render(request, 'index.html', {'userid': customer.cusid , 'userEmail' : customer.email})
        else:
            request.session['userid'] = None
            return redirect('login')
    else:
        admin = Admin.objects.get(adminid=Email)
        if admin is not None:
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


def updateCus(request , id_cus):
    cus = Customer.objects.get(cus_index = id_cus)
    print(id_cus)
    Email = request.POST['Edit_Email']
    Nic = request.POST['Edit_Nic']
    line1 = request.POST['AddressLineOne']
    line2 = request.POST['Edit_AddLine2']
    pCode = request.POST['Edit_PCode']
    fname = request.POST['Edit_Fname']
    lname = request.POST['Edit_Lname']
    print("cusname " + lname)
    
    cus2 = Customer(cus_index=id_cus , f_name=fname, l_name=lname,  email=Email,
        address_l1=line1, address_l2=line2, postcode=pCode, cusnic=Nic , )
    cus.save()
    cus1 = Customer.objects.get(cusid=request.session['userid'])
    return render(request, 'User_profile.html', {'customer': cus2})
    # form = custmoneForm(request.POST , instance = cus)
    # if form.is_valid:
    #     form.save()
    #     cus1 = Customer.objects.get(cusid=request.session['userid'])
    #     return render(request, 'User_profile.html', {'customer': cus1})


def adduser(request):

    rand = generateRandomeNum()

    addEmpEID = "EMP" + rand.fiveNums()
    print("custId" + addEmpEID)

    addEmpFname = request.GET['addEmpFname']
    addEmpLname = request.GET['addEmpLname']
    addEmpNIC = request.GET['addEmpNIC']
    #addEmpMale = request.GET['addEmpMale']
    addEmpEmail = request.GET['addEmpEmail']

    addEmpPhone = request.GET['addEmpPhone']
    addEpLineOne = request.GET['addEpLineOne']
    addEpLineTwo = request.GET['addEpLineTwo']
    addEmpcity = request.GET['addEmpcity']
    addEmpPCode = request.GET['addEmpPCode']
    addempDateOfJoin = request.GET['addempDateOfJoin']
    addempSal = request.GET['addempSal']
    addempOTRate = request.GET['addempOTRate']

    employee = Employee(empid=addEmpEID, f_name=addEmpFname,
                        l_name=addEmpLname, empnic=addEmpNIC, gender='Male',    email=addEmpEmail, phone=addEmpPhone,
                        address_l1=addEpLineOne, address_l2=addEpLineTwo, postcode=addEmpPCode, reg_date=addempDateOfJoin, basic_sal=addempSal,
                        ot_rate=addempOTRate)
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
