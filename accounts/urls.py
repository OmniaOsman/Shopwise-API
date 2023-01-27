from django.urls import path
from accounts.views import RegisterUserAPIView

urlpatterns = [
    # path("get-details", UserDetailAPI.as_view()),
    path("register", RegisterUserAPIView.as_view()),
]
