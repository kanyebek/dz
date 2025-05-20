from django.urls import path
from users.views import register, login_view, logout_view, confirm_user

urlpatterns = [
    path('register/', register),
    path('login/', login_view),
    path('logout/', logout_view),
    path('confirm/', confirm_user),
]