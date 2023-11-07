from rest_framework import generics
from .models import Scoreboard
from .serializers import ScoreboardSerializer
from rest_framework import permissions
# Create your views here.

class ScoreboardList(generics.ListCreateAPIView):
    queryset = Scoreboard.objects.all()
    serializer_class = ScoreboardSerializer
    permission_classes = [permissions.IsAuthenticated]

class ScoreboardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scoreboard.objects.all()
    serializer_class = ScoreboardSerializer
    permission_classes = [permissions.IsAuthenticated]
