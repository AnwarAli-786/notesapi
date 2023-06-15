from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    TEXT = 'text'
    AUDIO = 'audio'
    VIDEO = 'video'
    NOTE_TYPES = (
        (TEXT, 'Text'),
        (AUDIO, 'Audio'),
        (VIDEO, 'Video'),
    )

    content = models.TextField()
    type = models.CharField(max_length=5, choices=NOTE_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
