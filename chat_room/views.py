from django.http import HttpResponseRedirect
from django.shortcuts import render

from chat_room.forms import ChatForm


def index_view(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        # If not valid, previously filled form will be presented in HTML
        if form.is_valid():
            return HttpResponseRedirect(f'/chat/{form.cleaned_data["room_name"]}/')
    else:
        form = ChatForm()

    return render(request, 'index.html', {'form': form})


def room_view(request, room_name):
    context = {
        "room_name": room_name
    }
    return render(request, 'room.html', context)
