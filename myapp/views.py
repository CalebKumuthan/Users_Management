from rest_framework import generics
from .models import Admin_Users, Admin_Roles
from .serializer import UsersSerializer
from rest_framework.response import Response


#Kumuthan 05/07/2023    
class ListUsers(generics.ListAPIView, generics.CreateAPIView): #To list all users and to create new user.
    queryset = Admin_Users.objects.all()
    serializer_class = UsersSerializer

#Kumuthan 05/07/2023    
class DetailedUsers(generics.RetrieveUpdateDestroyAPIView): #To retrieve, update and delete particular user.
    queryset = Admin_Users.objects.all()
    serializer_class = UsersSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        self.perform_destroy(instance)
        return Response(serializer.data, status=204)