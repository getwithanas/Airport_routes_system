from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_route, name='add-route'), # Add new airport route
    path('nth-node/', views.nth_node_view, name='nth-node'), # View to get the nth node in a direction
    path('longest/', views.longest_route_view, name='longest-route'), # View to get the longest route
    path('shortest/', views.shortest_route_view, name='shortest-route'), # View to get the shortest route between two airports
]