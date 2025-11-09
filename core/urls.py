from django.urls import include, path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("terms_and_conditions",views.terms_and_conditions,name="terms_and_conditions"),
    path("privacy_policy",views.privacy_policy,name="privacy_policy"),
    path("accounts/signup/",views.signup,name="signup"),
    path("accounts/login/", views.user_login, name="login"),
    path("accounts/logout/", views.logout, name="logout"),
]