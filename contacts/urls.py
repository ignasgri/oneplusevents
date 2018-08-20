from django.conf.urls import url
from contacts.views import *


urlpatterns = [
   url(r'^$', contacts, name='contacts'),    
]