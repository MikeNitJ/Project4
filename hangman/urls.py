# URLS

from django.urls import path
from .views import ScoreboardList, ScoreboardDetail

urlpatterns = [
    path('scoreboard/', ScoreboardList.as_view(), name='scoreboard-list'),
    path('scoreboard/<int:pk>/', ScoreboardDetail.as_view(), name='scoreboard-detail'),

]