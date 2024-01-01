from django.urls import path
from .views import *

urlpatterns = [
    path('', landing_page, name="landing"),
    path('create-account/', create_user, name="create_account"),
    path('update-account/<int:pk>/', update_user, name="update_user"),
    path('profile/', view_profile, name='view_profile'),
    path('login/', login_page, name="login"),
    path('logout/', logout_page, name="logout"),
    path('password-change/', password_change, name="change_password"),
    path('password-change-done/', password_change_done, name="password_change_done"),
]
