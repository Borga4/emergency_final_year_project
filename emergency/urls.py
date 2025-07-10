from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
# from . import views
from accounts.views import login_view
from .views import analysis_view
from django.contrib.auth import views as auth_views
from .views import *
from accounts.views import *

urlpatterns = [
    
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('home/', index, name='home'),
    path('pending_cases/', pending_cases_page, name='pending_cases_page'),
    path('resolved_cases/', resolved_cases_page, name='resolved_cases_page'),
    path('analysis/', analysis_view, name='analysis_view'),
    path('logout/', logout_view, name='logout'),
]


# urlpatterns = [
#     # path('signup/', signup_view, name='signup'),
#     path('login/', login_view, name='login'),
# ]


    




