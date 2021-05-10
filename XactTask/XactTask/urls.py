from django.conf.urls import url
import django.contrib.auth.views
from app.views import home
from datetime import datetime
import app.forms
import app.views


urlpatterns = [
    url(r'^$', app.views.home, name='home'),
    #url(r'^home/$', app.views.home, name='home'),
]
