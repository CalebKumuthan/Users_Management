from django.shortcuts import render,redirect
from rest_framework import generics
from .models import Kumuthan_Users, Kumuthan_Role
from .serializer import ClientSerializer
from rest_framework.response import Response

# Create your views here.
    
class ListUsers(generics.ListAPIView, generics.CreateAPIView):
    queryset = Kumuthan_Users.objects.all()
    serializer_class = ClientSerializer

class DetailedUsers(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kumuthan_Users.objects.all()
    serializer_class = ClientSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        self.perform_destroy(instance)
        return Response(serializer.data, status=204)