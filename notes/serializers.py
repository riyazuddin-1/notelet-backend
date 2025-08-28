from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    _id = serializers.UUIDField(source='id', read_only=True)
    email = serializers.EmailField(read_only=True)
    title = serializers.CharField(allow_blank=True)
    content = serializers.CharField(allow_blank=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Note
        fields = ['_id' , 'email', 'title', 'content', 'created_at']
    
    def create(self, validated_data):
        request = self.context.get('request')
        user = None
        if request and request.user and request.user.is_authenticated:
            user = request.user
            validated_data['email'] = user.email
        return super().create(validated_data)

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'created_at']