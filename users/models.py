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

class User(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=9)
    email = models.EmailField(max_length=50)
    role = models.IntegerField(choices=Roles.choices, default=Roles.INACTIVE)
    password = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


