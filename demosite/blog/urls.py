from django.contrib.auth import views as authviews
from django.conf.urls import url
from . import views

urlpatterns = [
    url(R'^$', views.post_list, name='post_list'),
    url(R'^post/new/$', views.post_new, name='post_new'),
    url(R'^login/$', authviews.login, name='login'),
    url(R'^logout/$', authviews.logout, {'next_page': 'post_list'}, name='logout'),
]
