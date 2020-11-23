from django import forms


class ChatForm(forms.Form):
    room_name = forms.CharField(label='Enter room name', max_length=20)
    user_name = forms.CharField(label='Enter your name', max_length=20)
