from django.urls import path
from .views import ProductViewer

urlpatterns = [
    path('/products', ProductViewer.as_view()),
]