from django.urls import path

from chat_room.views import login_view, index_view, room_view


urlpatterns = [
    path('', login_view, name='login'),
    path('rooms/', index_view, name='index'),
    path('room/', room_view, name='room'),
]
