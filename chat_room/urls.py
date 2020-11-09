from django.urls import path

from chat_room.views import index_view


urlpatterns = [
    path('', index_view, name='index'),
]
