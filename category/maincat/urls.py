from django.conf.urls import url
from .import views


app_name = 'maincat'

urlpatterns = [
    url(r'^$', views.maincatIndex, name="list"),
    url(r'^add/$', views.maincatAdd, name="add"),
    url(r'^(?P<id>.*)/$', views.maincatEdit, name="change"),
    url(r'^(?P<id>[\w-]+)/$', views.maincatDelete, name="delete"),
]