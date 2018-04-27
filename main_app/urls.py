from django.conf.urls import url
from .views import index, detail, post_treasure, profile, login_view, logout_view

urlpatterns = [
    url(r'^$', index),
    url(r'^([0-9]+)/$',
    detail, name='detail'),
    url(r'^post_url/$', post_treasure, name='post_treasure'),
    url(r'^user/(\w+)/$', profile, name='profile'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout')
]