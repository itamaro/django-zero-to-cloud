from django.conf.urls import url
from . import views

urlpatterns = [
    url(R'^(?P<pizza_id>[0-9]+)/$',
        views.pizza_info, name='detail'),
    url(R'^$', views.index, name='index'),
]
