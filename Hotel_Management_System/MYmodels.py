# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    emp_index = models.AutoField(db_column='emp_Index', primary_key=True)  # Field name made lowercase.
    adminid = models.CharField(db_column='adminId', max_length=6)  # Field name made lowercase.
    empid = models.CharField(db_column='empId', max_length=6)  # Field name made lowercase.
    password = models.CharField(max_length=10, blank=True, null=True)
    last_login = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class Answers(models.Model):
    ansid = models.CharField(db_column='ansId', primary_key=True, max_length=8)  # Field name made lowercase.
    feedbackid = models.ForeignKey('Feedback', models.DO_NOTHING, db_column='feedbackId')  # Field name made lowercase.
    type = models.CharField(max_length=20, blank=True, null=True)
    empid = models.CharField(db_column='empId', max_length=6, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answers'
        unique_together = (('ansid', 'feedbackid'),)


class Attendencesheet(models.Model):
    empid = models.CharField(db_column='empId', primary_key=True, max_length=6)  # Field name made lowercase.
    date = models.DateField()
    timein = models.TimeField(db_column='timeIn')  # Field name made lowercase.
    timeout = models.TimeField(db_column='timeOut')  # Field name made lowercase.
    noofhours = models.IntegerField(db_column='NoOfHours', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendencesheet'
        unique_together = (('empid', 'date'),)


class Attraction(models.Model):
    attractionid = models.CharField(db_column='attractionID', primary_key=True, max_length=6)  # Field name made lowercase.
    img = models.CharField(max_length=250, blank=True, null=True)
    discription = models.CharField(db_column='Discription', max_length=350, blank=True, null=True)  # Field name made lowercase.
    distance = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attraction'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CardPayment(models.Model):
    paymentid = models.CharField(db_column='paymentId', primary_key=True, max_length=8)  # Field name made lowercase.
    cusid = models.CharField(db_column='cusId', max_length=8)  # Field name made lowercase.
    reportid = models.CharField(db_column='reportID', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ammount = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    cardno = models.CharField(db_column='cardNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    crcno = models.IntegerField(db_column='crcNo', blank=True, null=True)  # Field name made lowercase.
    expdate = models.DateField(db_column='expDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'card_payment'


class CardpaymentCardpayment(models.Model):
    month = models.CharField(db_column='Month', max_length=20)  # Field name made lowercase.
    card_number = models.CharField(db_column='Card_number', max_length=100)  # Field name made lowercase.
    exp_date = models.CharField(db_column='Exp_date', max_length=100)  # Field name made lowercase.
    crc = models.CharField(db_column='CRC', max_length=100)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount')  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cardpayment_cardpayment'


class Cardvalidation(models.Model):
    cardnum = models.IntegerField(db_column='cardNum', primary_key=True)  # Field name made lowercase.
    crc = models.IntegerField(db_column='CRC')  # Field name made lowercase.
    expdate = models.DateTimeField(db_column='expDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cardvalidation'


class CashPayment(models.Model):
    paymentid = models.CharField(db_column='paymentId', primary_key=True, max_length=8)  # Field name made lowercase.
    cusid = models.CharField(db_column='cusId', max_length=8)  # Field name made lowercase.
    reportid = models.CharField(db_column='reportID', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ammount = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_payment'


class CashpaymentCashpayment(models.Model):
    item_type = models.CharField(db_column='Item_type', max_length=100)  # Field name made lowercase.
    item_number = models.CharField(db_column='Item_number', max_length=100)  # Field name made lowercase.
    quantity = models.CharField(db_column='Quantity', max_length=100)  # Field name made lowercase.
    net_amount = models.FloatField(db_column='Net_amount')  # Field name made lowercase.
    month = models.CharField(db_column='Month', max_length=20)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cashpayment_cashpayment'


class Customer(models.Model):
    cus_index = models.AutoField(db_column='cus_Index', primary_key=True)  # Field name made lowercase.
    cusid = models.CharField(db_column='cusId', max_length=8)  # Field name made lowercase.
    cusnic = models.CharField(db_column='cusNIC', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f_name = models.CharField(db_column='f_Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    l_name = models.CharField(db_column='l_Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    address_l1 = models.CharField(db_column='address_L1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    address_l2 = models.CharField(db_column='address_L2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    postcode = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=150, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=6, blank=True, null=True)
    password = models.CharField(max_length=10, blank=True, null=True)
    last_login = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerFeed(models.Model):
    cusid = models.CharField(db_column='cusId', primary_key=True, max_length=8)  # Field name made lowercase.
    feedbackid = models.CharField(db_column='feedbackId', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer_feed'
        unique_together = (('cusid', 'feedbackid'),)


class CustomizedFooditems(models.Model):
    foodid = models.CharField(db_column='foodId', primary_key=True, max_length=8)  # Field name made lowercase.
    itemno = models.ForeignKey('Foodmenuitems', models.DO_NOTHING, db_column='ItemNo')  # Field name made lowercase.
    description = models.CharField(max_length=250, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customized_fooditems'
        unique_together = (('foodid', 'itemno'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    emp_index = models.AutoField(db_column='emp_Index', primary_key=True)  # Field name made lowercase.
    empid = models.CharField(db_column='empId', max_length=8, blank=True, null=True)  # Field name made lowercase.
    empnic = models.CharField(db_column='empNIC', max_length=10, blank=True, null=True)  # Field name made lowercase.
    faceid = models.CharField(db_column='faceID', max_length=500, blank=True, null=True)  # Field name made lowercase.
    f_name = models.CharField(db_column='f_Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    l_name = models.CharField(db_column='l_Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    address_l1 = models.CharField(db_column='address_L1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    address_l2 = models.CharField(db_column='address_L2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    postcode = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)
    basic_sal = models.FloatField(db_column='basic_Sal', blank=True, null=True)  # Field name made lowercase.
    ot_rate = models.FloatField(db_column='OT_Rate', blank=True, null=True)  # Field name made lowercase.
    reg_date = models.DateField(db_column='reg_Date', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=150, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=15, blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    last_login = models.CharField(max_length=150, blank=True, null=True)
    occu = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Feedback(models.Model):
    feedbackid = models.CharField(db_column='feedbackId', primary_key=True, max_length=8)  # Field name made lowercase.
    category = models.CharField(max_length=20, blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback'


class FoodPromotion(models.Model):
    promotionid = models.CharField(db_column='promotionId', primary_key=True, max_length=8)  # Field name made lowercase.
    description = models.CharField(max_length=250, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    image = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_promotion'


class Foodmenuitems(models.Model):
    itemno = models.CharField(db_column='ItemNo', primary_key=True, max_length=8)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=250, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    image = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'foodmenuitems'


class Foodorder(models.Model):
    orderid = models.CharField(db_column='orderId', primary_key=True, max_length=8)  # Field name made lowercase.
    cusid = models.CharField(db_column='cusId', max_length=8)  # Field name made lowercase.
    price = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'foodorder'


class FoodorderFoodPromotion(models.Model):
    promotionid = models.CharField(db_column='promotionId', primary_key=True, max_length=8)  # Field name made lowercase.
    orderid = models.ForeignKey(Foodorder, models.DO_NOTHING, db_column='orderId')  # Field name made lowercase.
    no_ofitems = models.IntegerField(db_column='No_ofItems', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'foodorder_food_promotion'
        unique_together = (('promotionid', 'orderid'),)


class FoodorderFoodmenuitem(models.Model):
    orderid = models.OneToOneField(Foodorder, models.DO_NOTHING, db_column='orderId', primary_key=True)  # Field name made lowercase.
    itemno = models.ForeignKey(Foodmenuitems, models.DO_NOTHING, db_column='ItemNo')  # Field name made lowercase.
    noofitems = models.FloatField(db_column='NoofItems', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'foodorder_foodmenuitem'
        unique_together = (('orderid', 'itemno'),)


class Hotelpackage(models.Model):
    hp_packageid = models.CharField(db_column='HP_packageID', primary_key=True, max_length=8)  # Field name made lowercase.
    pack_name = models.CharField(db_column='Pack_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=30, blank=True, null=True)
    img = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotelpackage'


class HotelpackageFoodmenuitem(models.Model):
    hp_packageid = models.OneToOneField(Hotelpackage, models.DO_NOTHING, db_column='HP_packageID', primary_key=True)  # Field name made lowercase.
    itemno = models.ForeignKey(Foodmenuitems, models.DO_NOTHING, db_column='ItemNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hotelpackage_foodmenuitem'
        unique_together = (('hp_packageid', 'itemno'),)


class Hotelpackagebooking(models.Model):
    hp_reserveid = models.CharField(db_column='HP_reserveID', primary_key=True, max_length=8)  # Field name made lowercase.
    hp_packageid = models.ForeignKey(Hotelpackage, models.DO_NOTHING, db_column='HP_packageID')  # Field name made lowercase.
    cusid = models.CharField(db_column='cusId', max_length=8)  # Field name made lowercase.
    date = models.DateTimeField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    noofpeole = models.IntegerField(db_column='NoOfPeole', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hotelpackagebooking'


class IncludeTourguide(models.Model):
    guideid = models.OneToOneField('Tourguide', models.DO_NOTHING, db_column='guideId', primary_key=True)  # Field name made lowercase.
    tourid = models.ForeignKey('Tour', models.DO_NOTHING, db_column='tourID')  # Field name made lowercase.
    time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'include_tourguide'
        unique_together = (('guideid', 'tourid'),)


class Ingredients(models.Model):
    ingredientid = models.CharField(db_column='ingredientId', primary_key=True, max_length=8)  # Field name made lowercase.
    name = models.CharField(max_length=20, blank=True, null=True)
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    availableammount = models.IntegerField(db_column='availableAmmount', blank=True, null=True)  # Field name made lowercase.
    limit_min = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredients'


class Invoice(models.Model):
    invoiceid = models.CharField(db_column='invoiceID', max_length=8)  # Field name made lowercase.
    cusid = models.CharField(db_column='cusId', max_length=8)  # Field name made lowercase.
    hp_reserveid = models.OneToOneField(Hotelpackagebooking, models.DO_NOTHING, db_column='HP_reserveID', primary_key=True)  # Field name made lowercase.
    r_reserveid = models.ForeignKey('Roomreservation', models.DO_NOTHING, db_column='R_reserveID')  # Field name made lowercase.
    rh_reserveid = models.ForeignKey('Receptionhallbooking', models.DO_NOTHING, db_column='RH_reserveID')  # Field name made lowercase.
    date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    totalammount = models.FloatField(db_column='totalAmmount', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice'


class PaymentReport(models.Model):
    reportid = models.CharField(db_column='reportId', primary_key=True, max_length=8)  # Field name made lowercase.
    month = models.DateField()
    income = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_report'


class Receptionhallbooking(models.Model):
    rh_reserveid = models.CharField(db_column='RH_reserveID', primary_key=True, max_length=8)  # Field name made lowercase.
    cusid = models.CharField(db_column='cusId', max_length=8)  # Field name made lowercase.
    theme = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    timefrom = models.TimeField(db_column='timeFrom', blank=True, null=True)  # Field name made lowercase.
    timeto = models.TimeField(db_column='timeTo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'receptionhallbooking'


class ReceptionhallbookingFoodmenuitems(models.Model):
    itemno = models.OneToOneField(Foodmenuitems, models.DO_NOTHING, db_column='ItemNo', primary_key=True)  # Field name made lowercase.
    rh_packageid = models.ForeignKey('Receptionhallpackage', models.DO_NOTHING, db_column='RH_packageID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'receptionhallbooking_foodmenuitems'
        unique_together = (('itemno', 'rh_packageid'),)


class ReceptionhallbookingPackage(models.Model):
    rh_reserveid = models.OneToOneField(Receptionhallbooking, models.DO_NOTHING, db_column='RH_reserveID', primary_key=True)  # Field name made lowercase.
    rh_packageid = models.ForeignKey('Receptionhallpackage', models.DO_NOTHING, db_column='RH_packageID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'receptionhallbooking_package'
        unique_together = (('rh_reserveid', 'rh_packageid'),)


class Receptionhallpackage(models.Model):
    rh_packageid = models.CharField(db_column='RH_packageID', primary_key=True, max_length=8)  # Field name made lowercase.
    theme = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=30, blank=True, null=True)
    img = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'receptionhallpackage'


class RevokedPayment(models.Model):
    revid = models.CharField(db_column='revId', primary_key=True, max_length=8)  # Field name made lowercase.
    paymentid = models.CharField(db_column='paymentId', max_length=8)  # Field name made lowercase.
    revammount = models.FloatField(db_column='revAmmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'revoked_payment'
        unique_together = (('revid', 'paymentid'),)


class Room(models.Model):
    roomno = models.CharField(db_column='RoomNo', primary_key=True, max_length=8)  # Field name made lowercase.
    type = models.CharField(max_length=10, blank=True, null=True)
    space = models.CharField(max_length=10, blank=True, null=True)
    unitprice = models.FloatField(db_column='Unitprice', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=30, blank=True, null=True)
    img = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room'


class Roomreservation(models.Model):
    r_reserveid = models.CharField(db_column='R_reserveID', primary_key=True, max_length=8)  # Field name made lowercase.
    cusid = models.CharField(db_column='cusId', max_length=8)  # Field name made lowercase.
    checkinttime = models.DateTimeField(db_column='checkIntTime', blank=True, null=True)  # Field name made lowercase.
    checkouttime = models.DateTimeField(db_column='checkOutTime', blank=True, null=True)  # Field name made lowercase.
    noofrooms = models.IntegerField(db_column='NoOfRooms', blank=True, null=True)  # Field name made lowercase.
    noofpeole = models.IntegerField(db_column='NoOfPeole', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roomreservation'


class RoomreservationRoom(models.Model):
    r_reserveid = models.OneToOneField(Roomreservation, models.DO_NOTHING, db_column='R_reserveID', primary_key=True)  # Field name made lowercase.
    roomno = models.ForeignKey(Room, models.DO_NOTHING, db_column='RoomNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roomreservation_room'
        unique_together = (('r_reserveid', 'roomno'),)


class Salarysheet(models.Model):
    empid = models.CharField(db_column='empId', max_length=6)  # Field name made lowercase.
    month = models.IntegerField(primary_key=True)
    totalsal = models.FloatField(db_column='totalSal', blank=True, null=True)  # Field name made lowercase.
    otallowences = models.FloatField(db_column='OTAllowences', blank=True, null=True)  # Field name made lowercase.
    otherallowences = models.FloatField(db_column='OtherAllowences', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salarysheet'
        unique_together = (('month', 'empid'),)


class Supplier(models.Model):
    supplierid = models.CharField(db_column='supplierId', primary_key=True, max_length=8)  # Field name made lowercase.
    f_name = models.CharField(db_column='f_Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    l_name = models.CharField(db_column='l_Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    address_l1 = models.CharField(db_column='address_L1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    address_l2 = models.CharField(db_column='address_L2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    postcode = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=150, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier'


class SupplierIngredients(models.Model):
    supplierid = models.OneToOneField(Supplier, models.DO_NOTHING, db_column='supplierId', primary_key=True)  # Field name made lowercase.
    ingredientid = models.ForeignKey(Ingredients, models.DO_NOTHING, db_column='ingredientId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supplier_ingredients'
        unique_together = (('supplierid', 'ingredientid'),)


class Tour(models.Model):
    tourid = models.CharField(db_column='tourID', primary_key=True, max_length=8)  # Field name made lowercase.
    location = models.CharField(max_length=20, blank=True, null=True)
    maxnoofpeople = models.IntegerField(db_column='maxNoOfPeople', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=30, blank=True, null=True)
    img = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tour'


class Tourguide(models.Model):
    guideid = models.CharField(db_column='guideId', primary_key=True, max_length=8)  # Field name made lowercase.
    f_name = models.CharField(db_column='f_Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    l_name = models.CharField(db_column='l_Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    address_l1 = models.CharField(db_column='address_L1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    address_l2 = models.CharField(db_column='address_L2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    postcode = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=150, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tourguide'
