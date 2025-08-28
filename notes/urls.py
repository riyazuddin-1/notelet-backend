from django.urls import path
from .views import CreateNote, ReadNote, UpdateNote, DeleteNote, NotesList

urlpatterns = [
    path('create', CreateNote.as_view(), name='Create note'),
    path('read', ReadNote.as_view(), name = 'Read note'),
    path('update', UpdateNote.as_view(), name = 'Update note'),
    path('delete', DeleteNote.as_view(), name='Delete note'),
    path('list', NotesList.as_view(), name='Notes list')
]