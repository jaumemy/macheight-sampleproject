from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('player_detail/', views.player_detail, name='player-detail'),
    path('player_matches/', views.player_matches, name='player-matches'),
    # path('playerlist/', views.PlayerListView, name='playerlist'),
]
