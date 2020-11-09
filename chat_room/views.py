from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')


def room_view(request, room_name):
    context = {
        "room_name": room_name
    }
    return render(request, 'room.html', context)
