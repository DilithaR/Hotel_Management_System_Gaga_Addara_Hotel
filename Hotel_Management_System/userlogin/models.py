# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Employee(models.Model):
    # Field name made lowercase.
    empid = models.CharField(db_column='empId', primary_key=True, max_length=6)
    # Field name made lowercase.
    empnic = models.CharField(db_column='empNIC', max_length=10)
    # Field name made lowercase.
    faceid = models.CharField(db_column='faceID', max_length=500)
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
    img = models.CharField(max_length=250, blank=True, null=True)
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

    class Meta:
        managed = True
        db_table = 'Employee'


class Admin(models.Model):
    # Field name made lowercase.
    adminid = models.CharField(
        db_column='adminId', primary_key=True, max_length=6)
    # Field name made lowercase.
    empid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='empId')
    password = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'admin'
        unique_together = (('adminid', 'empid'),)


class Customer(models.Model):
    # Field name made lowercase.
    cusid = models.CharField(db_column='cusId', primary_key=True, max_length=8)
    # Field name made lowercase.
    cusnic = models.CharField(db_column='cusNIC', max_length=10)
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
    img = models.CharField(max_length=250, blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='Email', max_length=150, blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    password = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'customer'

    # def __init__(self, cusid, cusnic, f_name, l_name, address_l1, address_l2, postcode, img, email, gender, password, phone):

    #     self.cusid = cusid
    #     self.cusnic = cusnic
    #     self.f_name = f_name
    #     self.l_name = l_name
    #     self.address_l1 = address_l1
    #     self.address_l2 = address_l2
    #     self.postcode = postcode
    #     self.img = img
    #     self.email = email
    #     self.gender = gender
    #     self.password = password
    #     self.phone = phone
