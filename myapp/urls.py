from django.urls import path
from . import views
app_name = "myapp"
urlpatterns = [
    path('users/', views.ListUsers.as_view(), name ='lpg'),
    path('users/<int:pk>/', views.DetailedUsers.as_view(), name = 'dpg'),
]