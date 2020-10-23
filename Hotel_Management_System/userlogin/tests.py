from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse
from userlogin.models import Employee , Customer
from faceRecognitionAttendence.models import Attendencesheet
import json

# Create your tests here.


def setCustoomer(self):
    self.client = Client()
    self.EditUserURl = reverse('updateCus')
    self.CUS00001 = Employee.objects.create(
        cusid= 'CUS00001',
        cusnic= '782596458V',
        f_name= 'Nuwan',
        l_name= 'Kulasekara' , 
        address_l1= 'No 2/A258',
        address_l2= 'Piliyandala',
        postcode= 22598,
        email= 'nuwankulasekara@gmail.com',
        gender= 'Male',
        password= '123ABC'
    )

def testUpdateCustomer(self):

    self.EditUserURl = reverse('updateCus')

    response = self.client.get(EditUserURl , {
        
        'first_Name'='Saman',
        'last_Name'='Thilakarathne',
        "address_line_1"='No 6/259B',
        "address_line_2"='Kesbewa',
        "postcode"=22569,
        'u_email'='samathilakarathne@gmail.com',
        'gender'='Male',

    })

    self.assertEqual(response.status_code, 302)
    self.assertEqual(self.CUS00001.cusnic, 'Saman')
    self.assertEqual(self.CUS00001.l_name, 'Thilakarathne')
    self.assertEqual(self.CUS00001.address_l1, 'No 6/259B')
    self.assertEqual(self.CUS00001.address_l2, 'Kesbewa')
    self.assertEqual(self.CUS00001.postcode, 22569)
    self.assertEqual(self.CUS00001.email, 'samathilakarathne@gmail.com')


def testResetUserPassword(self):
    self.checkEmailForresetPwURl = reverse('forgetpassword')

    response = self.client.get(checkEmailForresetPwURl, {

        'CheckEmail'='samathilakarathne@gmail.com',
    })

    testUpdatePassword()
    self.assertEqual(response.status_code, 302)


def testUpdatePassword(self):
    self.resetPwURl = reverse('fogetPw3')
    response = self.client.get(checkEmailForresetPwURl, {

        'newPassword'='QAZ111',
    })

    self.assertEqual(response.status_code, 302)
    self.assertEqual(self.CUS00001.password, 'QAZ111')
    self.assertEqual(self.CUS00001.email, 'samathilakarathne@gmail.com')



