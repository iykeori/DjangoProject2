from django.conf.urls import url
from .import views


app_name = 'product'

urlpatterns = [
    url(r'^$', views.productIndex, name="list"),
    url(r'^add/$', views.productAdd, name="add"),
    url(r'^(?P<id>.*)/$', views.productEdit, name="change"),
    url(r'^(?P<id>[\w-]+)/$', views.productDelete, name="delete"),
]
