from django.db import models


# Team model
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# User model
class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        return self.email

# Activity model (already present, but update to link to User)
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    title = models.CharField(max_length=200)
    duration_minutes = models.PositiveIntegerField(default=0)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.date})"

# Workout model
class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Leaderboard model
class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.email} - {self.score}"

