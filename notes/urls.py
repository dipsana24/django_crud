from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),  # list view
    path('note/<int:pk>/', views.note_detail, name='note_detail'),  # detail view
    path('note/new/', views.note_create, name='note_create'),  # create
    path('note/<int:pk>/edit/', views.note_update, name='note_update'),  # update
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),  # delete
]