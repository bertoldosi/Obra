from django.urls import path

from Diary.views.home_page import Index
from Diary.views.login import Login
from Diary.views.logout import Logout
from Diary.views.recover_password import Recover_Password
from Diary.views.register_user import Register_User

urlpatterns = [
    #Login
    path('', Index, name='home_page'),
    path('', Login, name="login"),
    path('logout', Logout, name="logout"),
    #User
    path('register_user', Register_User, name="register_user"),
    path('recover_password', Recover_Password, name="recover_password"),
    #Customer
    
]
