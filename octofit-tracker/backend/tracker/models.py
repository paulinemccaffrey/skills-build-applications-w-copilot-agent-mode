from django.db import models

class Activity(models.Model):
    title = models.CharField(max_length=200)
    duration_minutes = models.PositiveIntegerField(default=0)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.date})"

