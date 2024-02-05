from django.db import models

class product(models.Model):
    name=models.CharField(max_length=150)
    description=models.TextField()
    price=models.DecimalField(max_digit=6,decimal_places=2)
    