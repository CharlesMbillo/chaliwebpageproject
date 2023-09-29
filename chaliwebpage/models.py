from django.db import models

# Create your models here.
# chaliwepage/models.py

from django.core.validators import EmailValidator, RegexValidator

class UserProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\d{10,15}$',
                message="Phone number must be 10-15 digits."
            )
        ]
    )
    email = models.EmailField(
        validators=[EmailValidator(message="Enter a valid email address.")]
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name
