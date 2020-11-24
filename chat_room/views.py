from django.shortcuts import render, HttpResponse, redirect

from chat_room.forms import ChatForm


def index_view(request):
    return render(request, 'index.html', {'form': ChatForm()})


def room_view(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            context = {
                "room_name": "ASDASDASD"
            }
            return render(request, 'room.html', context)
        else:
            return HttpResponse("Wrong data has been entered. Please try again", status=400)
    else:
        return redirect(index_view)
