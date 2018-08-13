from django.urls import path
from . import views

app_name='wisesaying'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('detail/<int:pk>', views.detailView.as_view(), name="detail"),
    path('signup/', views.signup, name='signup'),
    path('search/', views.postSearch.as_view(), name='search'),
    path('add/', views.AddWord.as_view(), name='add'),
]