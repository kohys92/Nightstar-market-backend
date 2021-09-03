from django.urls import path, include

urlpatterns = [
    path('bbmarket', include('users.urls')), 
]
