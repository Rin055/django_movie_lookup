from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    rating = models.FloatField()

    def __str__(self):
        return self.title

class Viewer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    is_subscribed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewer = models.ForeignKey(Viewer, on_delete=models.SET_NULL, null=True, blank=True)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.movie.title} - {self.score}"
