from rest_framework import serializers
from .models import Admin_Roles, Admin_Users

class UsersSerializer(serializers.ModelSerializer): #To serialize Admin_User table
    role_name = serializers.SerializerMethodField() #To get role_name from Roles table
    class Meta:
        model = Admin_Users
        fields = ['id','first_name','last_name', 'email', 'phone_no', 'role_id', 'role_name']
    
    def get_role_name(self, obj):
        client_id = obj
        return(client_id.role_id.role_name)