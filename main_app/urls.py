from django.conf.urls import url
from .views import index, detail, post_treasure, profile

urlpatterns = [
    url(r'^$', index),
    url(r'^([0-9]+)/$',
    detail, name='detail'),
    url(r'^post_url/$', post_treasure, name='post_treasure'),
    url(r'^user/(\w+)/$', profile, name='profile')
]