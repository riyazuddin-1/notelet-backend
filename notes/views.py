from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404

from .models import Note
from .serializers import NoteSerializer, ListSerializer


class NoteView(APIView):
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.request.method == "GET":
            return []
        return [permissions.IsAuthenticated()]

    # LIST or SINGLE READ
    def get(self, request):
        note_id = request.query_params.get("note_id")

        # Single note
        if note_id:
            note = get_object_or_404(Note, id=note_id)
            serializer = NoteSerializer(note)
            return Response(serializer.data)

        # List notes (authenticated user)
        user = request.user
        notes = Note.objects.filter(email=user.email)\
            .order_by('-created_at')\
            .only('id', 'title', 'created_at')

        serializer = ListSerializer(notes, many=True)
        return Response(serializer.data)

    # CREATE
    def post(self, request):
        serializer = NoteSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        note = serializer.save()

        return Response(
            {
                "detail": "Created notes successfully",
                "note_id": NoteSerializer(note).data["_id"]
            },
            status=status.HTTP_201_CREATED
        )

    # UPDATE
    def patch(self, request):
        note_id = request.data.get("note_id")
        if not note_id:
            return Response({"detail": "note_id required"}, status=400)

        note = get_object_or_404(Note, id=note_id, email=request.user.email)

        serializer = NoteSerializer(
            note,
            data=request.data,
            partial=True,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"detail": "Note updated successfully"})

    # DELETE
    def delete(self, request):
        note_id = request.data.get("note_id")
        if not note_id:
            return Response({"detail": "note_id required"}, status=400)

        note = get_object_or_404(Note, id=note_id, email=request.user.email)
        note.delete()

        return Response({"detail": "Note deleted"})