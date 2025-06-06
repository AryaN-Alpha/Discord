from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serialization import RoomSerializer
from ..models import Room

@api_view(['GET'])
def getRoutes(request):
    routes=['GET api/' ,'GET api/rooms', 'GET api/rooms/:id']
    # return JsonResponse(routes , safe=False)
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()  # if we try to directly send it as response it gives error such as "	
                                #Object of type Room is not JSON serializable"
    serializer = RoomSerializer(rooms , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request,pk):
    room= Room.objects.get(id=pk)
    serializer = RoomSerializer(room , many=False)
    return Response(serializer.data)