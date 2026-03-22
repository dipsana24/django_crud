from django.db import models

class Note(models.Model):
    """
    Represents a single note containing a title, text content,
    and the timestamp of when it was created.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title