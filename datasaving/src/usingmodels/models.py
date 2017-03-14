from django.db import models

class cust_details(models.Model):
    cust_name=models.CharField(max_length=20)
    cust_id=models.IntegerField()

    def __str__(self):
        return self.cust_name+ str(self.cust_id)

    class Meta:
        db_table="cust_details"

class personal_details(models.Model):
    first_name=models.CharField(max_length=20)


    def __str__(self):
        return self.first_name

    class Meta:
        db_table="personal_details"