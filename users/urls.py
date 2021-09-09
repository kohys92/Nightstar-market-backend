from django.urls import path

from users.views import SignUpView, LogInView, DuplicationView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/login', LogInView.as_view()), 
    path('/signup/duplication', DuplicationView.as_view()),
]