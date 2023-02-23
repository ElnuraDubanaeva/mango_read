from django.urls import path
from .views import RegisterView, LoginView, UserListView

from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(), name="auth_login"),
    path("register/", RegisterView.as_view(), name="auth_register"),
    path("users/", UserListView.as_view({"get": "list"}), name="users"),
    path("users/<int:id>/", UserListView.as_view({"get": "retrieve"}), name="users"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verify/", TokenVerifyView.as_view(), name="verify"),
]
