from django.urls import path
from .views import ProductViewer, DetailViewer

urlpatterns = [
    path('/lists', ProductViewer.as_view()),
    path('/<int:id>', DetailViewer.as_view()),
]