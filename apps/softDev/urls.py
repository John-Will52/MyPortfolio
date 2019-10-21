from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about$', views.about, name='about'),
    url(r'^resume$', views.resume, name='resume'),
    url(r'^workshop$', views.workshop, name='workshop'),
]