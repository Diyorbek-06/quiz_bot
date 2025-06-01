from django.urls import path
from pkg_resources import parse_version

from .views import index, ready_test
from .user_wievs import signup
urlpatterns = [
    path('', index, name='index'),
    #test urls
    path('<int:test_id', ready_test, name='ready_test'),
    #user urls
    path('signup', signup, name='signup'),
]