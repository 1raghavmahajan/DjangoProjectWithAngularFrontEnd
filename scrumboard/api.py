from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from .serializers import ListSerializer, CardSerializer
from .models import List, Card

#ViewSets: auto generates all the apis GET POST PUT DELETE for the model
class ListViewSet(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

#Views : handles the request from the client
#basic ListAPIView can only handle get requests and returns the list of that specific model
class BasicGETCard_View(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
