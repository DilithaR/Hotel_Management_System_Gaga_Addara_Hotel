from django.core.mail import send_mail

class Mailing:
    def __init__(self , subject , body , myemail , recipients):
        self.subject = subject
        self.body = body
        self.myemail = myemail
        self.recipients = recipients 
    
    def sendmail(self , subject, body, myemail, recipients):
        send_mail(self.subject , self.body, self.myemail, self.recipients, fail_silently=True)
