from django.shortcuts import render,redirect
from RHM.forms import ReceptionHallPackageForm
from RHM.forms import ReceptionHallBookForm
from RHM.models import ReceptionHallBook
from RHM.models import ReceptionHallPackage
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from io import BytesIO
import xhtml2pdf.pisa as pisa
from django.template.loader import get_template
from django.template.loader import get_template



#redirecting the requrest to the add page of RHM


#def home (request):
 #   return render(request,'RHM/addres.html')


def addrespackage (request):

    if request.method == "POST":
            
            insertdata = ReceptionHallPackage()
            insertdata.theme       = request.POST.get('theme')
            insertdata.price       = request.POST.get('price')
            insertdata.description = request.POST.get('description')
            
            obj1= ReceptionHallPackage(theme = insertdata.theme ,price = insertdata.price ,description = insertdata.description )
            obj1.save()
            #return render(request, 'addResPackage.html')
            return redirect('/viewResPackage')
    else:         
          return render(request, 'addResPackage.html')

def addres(request):

    if request.method == "POST":
            
           insertdata = ReceptionHallBook()
           insertdata.cusId       = request.POST.get('cusId')
           insertdata.theme       = request.POST.get('theme')
           insertdata.date        = request.POST.get('date')
           insertdata.timeFrom    = request.POST.get('timeFrom')
           insertdata.timeTo      = request.POST.get('timeTo')
            
           obj2= ReceptionHallBook(cusId = str(insertdata.cusId) ,theme = insertdata.theme ,date =insertdata.date , timeFrom = insertdata.timeFrom,timeTo = insertdata.timeTo)
           obj2.save()
           return redirect('/Cviewres')
    else:         
          return render(request, 'addres.html')          
   
def viewpack(request):
    viewpackages = ReceptionHallPackage.objects.all()
    return render(request,"viewResPackage.html",{'viewpackages':viewpackages})

def viewres(request):
    viewres = ReceptionHallBook.objects.all()
    return render(request,"viewres.html",{'viewres':viewres})
   
def Cviewpack(request):
    viewpackages = ReceptionHallPackage.objects.all()
    return render(request,"CviewResPackage.html",{'viewpackages':viewpackages})

def Cviewres(request):
    viewres = ReceptionHallBook.objects.all()
    return render(request,"Cviewres.html",{'viewres':viewres})



def delete (request, RH_packageID):
        viewpackages = ReceptionHallPackage.objects.get(RH_packageID=RH_packageID)
        viewpackages.delete()
        return redirect("/viewResPackage")


def deleteres (request, RH_reserveID):
        viewres = ReceptionHallBook.objects.get(RH_reserveID=RH_reserveID)
        viewres.delete()
        return redirect("/viewres")        

def edit(request,RH_packageID ):  
    viewpackages = ReceptionHallPackage.objects.get(RH_packageID=RH_packageID)  
    return render(request,'editResPackage.html', {'viewpackages':viewpackages})  

def update(request, RH_packageID):  
    viewpackages = ReceptionHallPackage.objects.get(RH_packageID=RH_packageID)  
    form = ReceptionHallPackageForm(request.POST, instance = viewpackages)  
    if form.is_valid():  
        form.save()  
        return redirect("/viewResPackage")
    return render(request, 'viewResPackage.html')        
    
def getPdfPage(request):
    package = ReceptionHallPackage.objects.all()  
      
    data = {'package':package}
    template = get_template("pdf_output.html")
    data_d = template.render(data)
    response = BytesIO()

    pdfpage = pisa.pisaDocument(BytesIO(data_d.encode("UTF-8")),response)
    return HttpResponse(response.getvalue(),content_type="application/pdf")
 
