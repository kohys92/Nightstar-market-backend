from orders.views import CartView
from django.urls import path
from .views import CartView, OrderView

urlpatterns = [
    path('/carts',       CartView.as_view()),
    path('/order-sheet', OrderView.as_view()),
]
