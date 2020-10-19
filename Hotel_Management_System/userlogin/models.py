# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import random


class Employee(models.Model):
    # Field name made lowercase.
    emp_index = models.AutoField(db_column='emp_Index', primary_key=True)
    # Field name made lowercase.
    empid = models.CharField(db_column='empId', max_length=6)
    # Field name made lowercase.
    empnic = models.CharField(
        db_column='empNIC', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    faceid = models.CharField(
        db_column='faceID', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    f_name = models.CharField(
        db_column='f_Name', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    l_name = models.CharField(
        db_column='l_Name', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    address_l1 = models.CharField(
        db_column='address_L1', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    address_l2 = models.CharField(
        db_column='address_L2', max_length=30, blank=True, null=True)
    postcode = models.IntegerField(blank=True, null=True)
    img = models.ImageField(default='python.png', null=True, blank=True)
    # Field name made lowercase.
    basic_sal = models.FloatField(db_column='basic_Sal', blank=True, null=True)
    # Field name made lowercase.
    ot_rate = models.FloatField(db_column='OT_Rate', blank=True, null=True)
    # Field name made lowercase.
    reg_date = models.DateField(db_column='reg_Date', blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='Email', max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    last_login = models.CharField(max_length=150, blank=True, null=True)
    occu = models.CharField(max_length=50, blank=True, null=True)

    

    class Meta:
        managed = True
        db_table = 'Employee'


class Admin(models.Model):
    # Field name made lowercase.
    emp_index = models.AutoField(db_column='emp_Index', primary_key=True)
    # Field name made lowercase.
    adminid = models.CharField(db_column='adminId', max_length=6)
    # Field name made lowercase.
    empid = models.CharField(db_column='empId', max_length=6)
    password = models.CharField(max_length=10, blank=True, null=True)
    last_login = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class Customer(models.Model):
    # Field name made lowercase.
    cus_index = models.AutoField(db_column='cus_Index', primary_key=True)
    # Field name made lowercase.
    cusid = models.CharField(db_column='cusId', max_length=8)
    # Field name made lowercase.
    cusnic = models.CharField(
        db_column='cusNIC', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    f_name = models.CharField(
        db_column='f_Name', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    l_name = models.CharField(
        db_column='l_Name', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    address_l1 = models.CharField(
        db_column='address_L1', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    address_l2 = models.CharField(
        db_column='address_L2', max_length=30, blank=True, null=True)
    postcode = models.IntegerField(blank=True, null=True)
    img = models.ImageField(default = 'python.png' , null = True , blank = True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='Email', max_length=150, blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    password = models.CharField(max_length=10, blank=True, null=True)
    last_login = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class generateRandomeNum:
   
    def fiveNums(self):
        num = random.randrange(1 , (10**5)-1)
        addZeros = '{:04}'.format(num)
        return addZeros
        # num = random.randint(0 , 99999)
        # print("Randome number is" + num)
        # return num
    


