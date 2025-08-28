from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authentication import TokenAuthentication
from .models import Note
from .serializers import NoteSerializer, ListSerializer
from django.shortcuts import get_object_or_404


class CreateNote(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = NoteSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        note = serializer.save()

        return Response({"detail": "Created notes successfully", "note_id": NoteSerializer(note).data["_id"]}, status=status.HTTP_201_CREATED)

class ReadNote(APIView):
    permission_classes = []

    def post(self, request):
        note_id = request.data.get("note_id")
        if not note_id:
            return Response({"detail": "note_id required"}, status=status.HTTP_400_BAD_REQUEST)

        note = get_object_or_404(Note, id=note_id)
        serializer = NoteSerializer(note)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateNote(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        note_id = request.data.get("note_id")
        if not note_id:
            return Response({"detail": "note_id required"}, status=status.HTTP_400_BAD_REQUEST)

        note = get_object_or_404(Note, id=note_id, email=request.user.email)
        serializer = NoteSerializer(note, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        note = serializer.save()
        return Response({"detail": "Note updated successfully."}, status=status.HTTP_200_OK)

class DeleteNote(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        note_id = request.data.get("note_id")
        if not note_id:
            return Response({"detail": "note_id required"}, status=status.HTTP_400_BAD_REQUEST)

        note = get_object_or_404(Note, id=note_id, email=request.user.email)
        note.delete()
        return Response({"detail": "Note deleted"}, status=status.HTTP_200_OK)

class NotesList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        list = Note.objects.filter(email=user.email).order_by('-created_at').only('id', 'title', 'created_at')
        serializer = ListSerializer(list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)