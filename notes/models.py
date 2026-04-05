from django.db import models
import uuid

# Create your models here.
class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, db_index=True)
    email = models.EmailField(db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.created_at})"