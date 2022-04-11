   
"""Reviews models"""

from django.db import models


class Review(models.Model):
    """Review model"""
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField()
    comments = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "reseña"
        verbose_name_plural = "reseñas"
        ordering = ["created_at"]
        unique_together = [['movie', 'user']]   
