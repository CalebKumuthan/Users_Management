from django.db import models

# Create your models here.

class Kumuthan_Role(models.Model):
    role_name = models.CharField(max_length = 20, unique = True)
    status = models.BooleanField(default = True)
    created_by = models.IntegerField(default = 1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField(default = 1)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.role_name

class Kumuthan_Users(models.Model):
    first_name = models.CharField(max_length = 50,)
    last_name=models.CharField(max_length = 50,)
    email = models.EmailField(unique = True)
    role_id = models.ForeignKey(Kumuthan_Role, on_delete = models.CASCADE)
    phone_no = models.BigIntegerField(unique = True)

    def __str__(self) -> str:
        return self.name

# class Settings(models.Model):
#     client = models.ForeignKey('Clients', models.DO_NOTHING, blank=True, null=True)
#     sms_notification = models.CharField(max_length=-1, blank=True, null=True)
#     email_notification = models.CharField(max_length=-1, blank=True, null=True)
#     language = models.IntegerField(blank=True, null=True)
#     currency = models.IntegerField(blank=True, null=True)
#     sms_gateway = models.IntegerField(blank=True, null=True)
#     email_gateway = models.IntegerField(blank=True, null=True)
#     map_gateway = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'settings'


# class Clients(models.Model):
#     name = models.CharField(max_length=-1, blank=True, null=True)
#     company_name = models.CharField(max_length=-1, blank=True, null=True)
#     pri_mobile_number = models.CharField(max_length=-1, blank=True, null=True)
#     sec_mobile_number = models.CharField(max_length=-1, blank=True, null=True)
#     mobile_verify = models.CharField(max_length=-1, blank=True, null=True)
#     primary_email = models.CharField(max_length=-1, blank=True, null=True)
#     secondary_email = models.CharField(max_length=-1, blank=True, null=True)
#     email_verify = models.CharField(max_length=-1, blank=True, null=True)
#     address = models.TextField(blank=True, null=True)
#     state = models.CharField(max_length=-1, blank=True, null=True)
#     city = models.CharField(max_length=-1, blank=True, null=True)
#     country = models.IntegerField(blank=True, null=True)
#     status = models.CharField(max_length=-1, blank=True, null=True)
#     created_by = models.IntegerField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_by = models.IntegerField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'clients'