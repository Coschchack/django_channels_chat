from django.urls import path

from chat_room.views import index_view, room_view


urlpatterns = [
    path('', index_view, name='index'),
    path('room/', room_view, name='room'),
]
