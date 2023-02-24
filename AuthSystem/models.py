from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDER_CHOICES = (
        ("Man", 'Masculin'),
        ("Woman", 'Feminin'),
    )


    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True)
    bio = models.CharField(
        max_length=300
    )

    def __str__(self):
        return self.username