from rest_framework import serializers
from .models import Kumuthan_Role, Kumuthan_Users

class ClientSerializer(serializers.ModelSerializer):
    role_name = serializers.SerializerMethodField()
    class Meta:
        model = Kumuthan_Users
        fields = ['id','first_name','last_name', 'email', 'phone_no', 'role_id', 'role_name']
    
    def get_role_name(self, obj):
        client_id = obj
        return(client_id.role_id.role_name)