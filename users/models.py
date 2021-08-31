from django.db import models

# Create your models here.

class User(models.Model):
    account_name  = models.CharField(max_length = 45)
    password      = models.CharField(max_length = 200)
    name          = models.CharField(max_length = 45)
    email         = models.CharField(max_length = 100)
    phone_number  = models.CharField(max_length = 40)
    address       = models.CharField(max_length = 200)
    
    gender_choice       = (
            ("Man", "M"),
            ("Woman", "W"),
            ("No Select", "N")
            )

    gender        = models.CharField(max_length = 10, choices = gender_choice)
    date_of_birth = models.DateField()

    class Meta:
        db_table = 'users'

