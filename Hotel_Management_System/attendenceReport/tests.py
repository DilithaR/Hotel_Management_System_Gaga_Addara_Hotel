from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse
from userlogin.models import Employee
from faceRecognitionAttendence.models import Attendencesheet
import json
# Create your tests here.
empCountList[] = ''

class viewTestForReport(TestCase):

    

    def setEmployee(self):
        self.client = Client()
        self.HtmlReportUrl = reverse('attendenceReport')
        self.EMP00001 = Employee.objects.create(
            empid="EMP00001",
            empnic="586945788V",
            faceid=None,
            f_name="Mahen",
            l_name="Perera",
            address_l1="No 14/34A",
            address_l2="Colombo 08",
            postcode=22458,
            basic_sal=50000.00,
            ot_rate=250.00,
            reg_date='2020-10-12',
            email="mahenperera@gmail.com",
            phone='0716589258',
            remark=None,
            rating=4,
            gender="Male",
            occu="Waiter",
        )

    def testDailyEmpAttendence(self):
        response = self.client.get(self.HtmlReportUrl)

        sampleAttendence = Attendencesheet.objects.create(
            empid=self.EMP00001,
            date='2020-10-20',
            timein='08:22:45',
            timeout='16:22:45',
            noofhours=None,
            status='Compleated'
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(empCountList.count(), 1)
        self.assertEqual(empCountList, 18)
        self.assertEqual(sampleAttendence.noofhours,  '08.00')

    def testEmpSalCalculation(self):
        response = self.client.get(self.HtmlReportUrl)

        sampleAttendence_1 = Attendencesheet.objects.create(
            empid=self.EMP00001,
            date='2020-10-20',
            timein='08:22:45',
            timeout='16:22:45',
            noofhours=None,
            status='Compleated'
        )
        sampleAttendence_2 = Attendencesheet.objects.create(
            empid=self.EMP00001,
            date='2020-10-20',
            timein='08:22:45',
            timeout='16:22:45',
            noofhours=None,
            status='Compleated'
        )
        sampleAttendence_3 = Attendencesheet.objects.create(
            empid=self.EMP00001,
            date='2020-10-20',
            timein='08:22:45',
            timeout='16:22:45',
            noofhours=None,
            status='Compleated'
        )

        url = reverse('CalcSalary')

        response = self.client.get(url , {
            'ExtraAllowneces' : 6000.00
        })



        self.assertEqual(response.status_code, 302)
        self.assertEqual(sampleAttendence, '08.00')
        self.assertEqual(empCountList.count(), 1)
        self.assertEqual(expected_Days, 18)

    def testAttendenceBasics(self):
        client = Client()
        response = client.get(reverse('attendenceReport'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'AttendenceReport.html')
