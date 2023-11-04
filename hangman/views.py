from rest_framework import generics
from .models import Scoreboard
from .serializers import ScoreboardSerializer

# Create your views here.

class ScoreboardList(generics.ListCreateAPIView):
    queryset = Scoreboard.objects.all()
    serializer_class = ScoreboardSerializer

class ScoreboardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scoreboard.objects.all()
    serializer_class = ScoreboardSerializer
