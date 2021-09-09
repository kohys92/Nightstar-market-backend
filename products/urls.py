from django.urls import path
from .views import ProductView, DetailView

urlpatterns = [
    path('/lists', ProductView.as_view()),
    path('/<int:product_id>', DetailView.as_view()),
]