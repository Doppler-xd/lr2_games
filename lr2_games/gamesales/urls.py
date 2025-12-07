from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.GameAdListView.as_view(), name='index'),
    path('genre/<int:genre_id>/', views.GameAdByGenreView.as_view(), name='by_genre'),
    path('add/', views.GameAdCreateView.as_view(), name='add'),
    path('<int:pk>/edit/', views.GameAdUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.GameAdDeleteView.as_view(), name='delete'),
]