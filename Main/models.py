from django.db import models
from AuthSystem.models import User


# Create your models here.
class Blogs(models.Model):
    title = models.CharField(
        max_length=50
        )
    content = models.CharField(
        max_length=5000,
        min_length=300)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_by'
    )
    created_at= models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title