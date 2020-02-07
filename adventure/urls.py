from django.conf.urls import url
from . import api

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('map', api.map_end),
    url('say', api.say),
    url('map', api.map_end)

]