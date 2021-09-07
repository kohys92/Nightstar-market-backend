from django.db import models

class User(models.Model):
    gender_choice = (
            ("M", "Male"),
            ("F", "Female"),
            ("NA", "Not Available")
            )

    account_name  = models.CharField(max_length = 45)
    password      = models.CharField(max_length = 200)
    name          = models.CharField(max_length = 45)
    email         = models.EmailField()
    phone_number  = models.CharField(max_length = 40)
    address       = models.CharField(max_length = 200)
    gender        = models.CharField(max_length = 10, choices = gender_choice)
    date_of_birth = models.DateField()

    class Meta:
        db_table = 'users'

