from django.db import models


class Attendencesheet(models.Model):
    # Field name made lowercase.
    empid = models.CharField(db_column='empId', primary_key=True, max_length=8)
    date = models.DateField()
    timein = models.TimeField(db_column='timeIn')  # Field name made lowercase.
    # Field name made lowercase.
    timeout = models.TimeField(db_column='timeOut', blank=True, null=True)
    # Field name made lowercase.
    noofhours = models.IntegerField(
        db_column='NoOfHours', blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendencesheet'
        unique_together = (('empid', 'date'),)
