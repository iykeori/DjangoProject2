from django.conf.urls import url, include
from django.contrib import admin
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from product import views as show

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^maincat/',include('maincat.urls')),
    url(r'^product/',include('product.urls')),
    url(r'^$', views.catIndex),
    # url(r'^catAdd/$', views.catAdd),
    # url(r'^catEdit/$', views.catEdit),
    url(r'^$', show.productIndex, name="home"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
