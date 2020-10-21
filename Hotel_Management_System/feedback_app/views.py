from django.shortcuts import render, redirect
from feedback_app.forms import FeedbackForm
from feedback_app.forms import AnswerForm
from feedback_app.models import Feedback

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template.loader import get_template

#from django.http import HttpResponse
#import pyodbc
 
# Create your views here.

#add fb customer
def addfeedback (request):
    if request.method == "POST":

            insertdata = Feedback()
            insertdata.category       = request.POST.get('category')
            insertdata.description       = request.POST.get('description')
        

            obj1= Feedback(category = insertdata.category ,description = insertdata.description )
            obj1.save()
            
            return redirect('/reviews')
    else:
            return render(request, 'addfeedback.html')
            
            #form = FeedbackForm(request.POST)
            #if form.is_valid():
                    #try:
                     #       form.save()
                      #      return redirect('/views')
                            
                    #except:
                     #       pass

            #else:
             #       form = FeedbackForm()
            #return render(request,'addfeedback.html',{'form':form}) 

#def addreply (request, feedbackId):
 #   if request.method == "POST":
#
 #           insertdata = Feedback()
  #          insertdata.ansDescription    = request.POST.get('ansDescription')
#
 #           obj2= Feedback(ansDescription = insertdata.ansDescription)
  #          obj2.save()
   #         #return render(request, 'addReply.html')
    #        return redirect("/dashboardFB")
    #else:
     #       return render(request, 'addReply.html')

#reply feedback
def editreply (request, feedbackId):
        feedbacks = Feedback.objects.get(feedbackId=feedbackId)
        return render(request, "addReply.html",{'feedbacks':feedbacks})

def updatereply (request, feedbackId):  
    feedbacks = Feedback.objects.get(feedbackId=feedbackId)  
    form = AnswerForm(request.POST, instance = feedbacks)  
    if form.is_valid():  
        form.save()  
        return redirect("/dashboardFB")  
    return render(request, 'addReply.html', {'feedbacks': feedbacks})  
          
    
#retriew fb admin
def undfb (request):
        feedbacks = Feedback.objects.all()
        #return render(request, 'undfb.html')
        return render(request, "dashboardFB.html",{'feedbacks':feedbacks})

#delete fb Admin
def delete (request, feedbackId):
        feedbacks = Feedback.objects.get(feedbackId=feedbackId)
        feedbacks.delete()
        messages.success(request, "Feedback deleted successfully")
        return redirect("/undfb")

#review page
def reviews (request):
        feedbacks = Feedback.objects.all()
        return render(request, "reviews.html",{'feedbacks':feedbacks})

# edit fb by admin
def edit (request, feedbackId):
        feedbacks = Feedback.objects.get(feedbackId=feedbackId)
        return render(request, "editfeedback.html",{'feedbacks':feedbacks})

def update (request, feedbackId):  
    feedbacks = Feedback.objects.get(feedbackId=feedbackId)  
    form = FeedbackForm(request.POST, instance = feedbacks)  
    if form.is_valid():  
        form.save()  
        return redirect("/undfb")  
    return render(request, 'undfb.html', {'feedbacks': feedbacks})  

#generate report
def getPdfPage(request):
    feedbacks = Feedback.objects.all()  
      
    data = {'feedbacks':feedbacks}
    template = get_template("pdf_output.html")
    data_d = template.render(data)
    response = BytesIO()

    pdfpage = pisa.pisaDocument(BytesIO(data_d.encode("UTF-8")),response)
    return HttpResponse(response.getvalue(),content_type="application/pdf")

 