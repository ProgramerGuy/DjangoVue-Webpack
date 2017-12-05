from django.conf.urls import url
from .views import index, oficinas, create

urlpatterns = [
    url(r'^$', index),
    url(r'^oficinas/',oficinas),
    url(r'^create/',create),
]
