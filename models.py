from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

CURRENT_YEAR = datetime.date.today().year

class Video(models.Model):
    MovieID = models.AutoField(primary_key=True)
    MovieTitle = models.CharField(max_length=200)
    Actor1Name = models.CharField(max_length=120, blank=True)
    Actor2Name = models.CharField(max_length=120, blank=True)
    DirectorName = models.CharField(max_length=120, blank=True)

    GENRE_CHOICES = [
        ("Comedy", "Comedy"),
        ("Romance", "Romance"),
        ("Action", "Action"),
        ("Drama", "Drama"),
        ("Horror", "Horror"),
        ("Sci-Fi", "Sci-Fi"),
        ("Animation", "Animation"),
        ("Other", "Other"),
    ]
    MovieGenre = models.CharField(max_length=20, choices=GENRE_CHOICES)

    ReleaseYear = models.PositiveIntegerField(
        validators=[MinValueValidator(1888), MaxValueValidator(CURRENT_YEAR + 1)]
    )

    def __str__(self):
        return f"{self.MovieTitle} ({self.ReleaseYear})"

