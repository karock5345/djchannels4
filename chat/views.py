from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Create your views here.
def index(request):

    return render(request, "chat/index.html")

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})


def send(request):
    channel_layer = get_channel_layer()
    channel_group_name = "chat_707"
    print('channel_group_name:' + channel_group_name)
    async_to_sync (channel_layer.group_send)(channel_group_name, {"type": "chat_message",'message':'from index'})

    return render(request, "chat/send.html")