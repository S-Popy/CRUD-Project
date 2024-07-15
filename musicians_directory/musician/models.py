from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(10),]
    )
    instrument_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
