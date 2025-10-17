from django.urls import path
from .views import NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path('', NoteListView.as_view(), name='note_list'),
    path('add/', NoteCreateView.as_view(), name='note_add'),
    path('edit/<int:pk>/', NoteUpdateView.as_view(), name='note_edit'),
    path('delete/<int:pk>/', NoteDeleteView.as_view(), name='note_delete'),
]
