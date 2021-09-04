from django.urls import path
from .views import ProductViewer

urlpatterns = [
    path('/lists', ProductViewer.as_view()),
]