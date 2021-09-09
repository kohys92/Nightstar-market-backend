from django.urls import path

from users.views import SignUpView, LogInView, AccountDuplicationView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/login', LogInView.as_view()), 
    path('/signup/duplication', AccountDuplicationView.as_view()),
]