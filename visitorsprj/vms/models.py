from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Visitor(models.Model):

    TITLE_CHOICES = [
        ("Mr.", "Mister"),
        ("Mrs.", "Mrs"),
        ("Miss.", "Miss"),
        ("Dr.", "Doctor"),
        ("Maj.", "Major"),
    ]

    HOST_CHOICES = [
        ("ALEX", "Alex"),
        ("SMITH", "Smith"),
        ("JOHNSON", "Johnson"),
        ("DOE", "Doe"),
        ("WILLIAMS", "Williams"),
    ]

    image = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    host = models.CharField(max_length=10, choices=HOST_CHOICES)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.image.url} {self.firstname} {self.lastname}"


