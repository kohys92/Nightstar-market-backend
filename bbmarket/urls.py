from django.urls import path, include

urlpatterns = [
    # path('bbmarket', include('users.urls')),
    path('bbmarket', include('products.urls')),
]
