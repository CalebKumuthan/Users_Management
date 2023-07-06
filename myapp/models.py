
from django.db import models

#To create roles model(table)
class Admin_Roles(models.Model):
    role_name = models.CharField(max_length = 20, unique = True)
    status = models.BooleanField(default = True)
    created_by = models.IntegerField(default = 1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField(default = 1)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.role_name

#To create users table
class Admin_Users(models.Model):
    first_name = models.CharField(max_length = 50,)
    last_name=models.CharField(max_length = 50,)
    email = models.EmailField(unique = True)
    role_id = models.ForeignKey(Admin_Roles, on_delete = models.CASCADE)
    phone_no = models.BigIntegerField(unique = True)

    def __str__(self) -> str:
        return self.name