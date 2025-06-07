from django.urls import path

from .views import index, ready_test, test
from .user_wievs import signup
urlpatterns = [
    path('', index, name='index'),
    #test urls
    path('<int:test_id>/ready_test', ready_test, name='ready_test'),
    path('<int:test_id>/test', test, name='test'),
    #user urls
    path('signup', signup, name='signup'),
]