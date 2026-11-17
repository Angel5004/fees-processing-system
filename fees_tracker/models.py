from django.db import models

# Create your models here.

class Classroom(models.Model):
    class_number = models.IntegerField()

class Academic_session(models.Model):
    STATUS_OPTIONS = [
        ("C", "Continuing"),
        ("E", "Ending"),
    ]
    year = models.IntegerField()
    term = models.CharField(max_length = 10)
    beginning_date = models.DateField()
    
    ending_date = models.DateField()
    status = models.CharField(max_length = 2, choices= STATUS_OPTIONS)

class Bill_items(models.Model):
    item_name = models.CharField(max_length= 20)
    item_cost = models.IntegerField()

class Pupil(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    class_number = models.CharField(max_length = 3)
    birth_date = models.DateField()
    address = models.CharField(max_length= 20)
    parent = models.CharField(max_length= 30)
    contact = models.CharField(max_length= 10) 

class Pupil_bill(models.Model):
    pupil_id = models.ForeignKey(Pupil, on_delete= models.CASCADE)
    academic_session_id = models.ForeignKey(Academic_session, on_delete= models.CASCADE)
    bill_item_id = models.ForeignKey(Bill_items, on_delete= models.CASCADE)
    amount = models.IntegerField()     

class Payment(models.Model):
    PAYMENT_OPTIONS = [
        ("CP", "Cash payment"),
        ("MP", "Mobile money")
    ]
    pupil_id = models.ForeignKey(Pupil, on_delete= models.CASCADE)
    pupil_bill_id = models.ForeignKey(Pupil_bill, on_delete = models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount_paid = models.IntegerField()
    payment_method = models.CharField(max_length = 2, choices= PAYMENT_OPTIONS)
    received_by = models.CharField(max_length= 20, blank = True, default = "")  



    