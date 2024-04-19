from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Roles(models.IntegerChoices):
    INACTIVE = 0, "inactive"
    CUSTOMER = 1, "customer"
    EMPLOYEE = 2, "employee"
    ADMIN = 3, "admin"
