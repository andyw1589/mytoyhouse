from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from folders.models import Folder

# Create your models here.
class Character(models.Model):
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_created=True, default=timezone.now)
    folder = models.ForeignKey(Folder, null=True, on_delete=models.CASCADE)

    # basics
    name = models.CharField(max_length=200, null=False)
    nicknames = models.CharField(max_length=200, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    sex = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    religion = models.CharField(max_length=100, null=True, blank=True)
    race = models.CharField(max_length=100, null=True, blank=True)
    species = models.CharField(max_length=100, null=True, blank=True)

    # birth related
    birthday = models.DateField(null=True, blank=True)
    birthplace = models.CharField(max_length=200, null=True, blank=True)

    # physical descriptions
    blood_type = models.CharField(max_length=5, null=True, blank=True)
    height = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)  # in meters
    weight = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)  # in kilograms
    eye_colour = models.CharField(max_length=50, null=True, blank=True)
    hair_colour = models.CharField(max_length=50, null=True, blank=True)
    eyesight = models.CharField(max_length=50, null=True, blank=True)
    dominant_hand = models.CharField(max_length=20, null=True, blank=True)
    voice = models.CharField(max_length=100, null=True, blank=True)
    physical_description = models.CharField(max_length=2000, null=True, blank=True)
    clothing = models.CharField(max_length=2000, null=True, blank=True)

    # history
    medical_history = models.CharField(max_length=2000, null=True, blank=True)
    criminal_record = models.CharField(max_length=2000, null=True, blank=True)
    education = models.CharField(max_length=2000, null=True, blank=True)
    forming_events = models.CharField(max_length=2000, null=True, blank=True)
    romance = models.CharField(max_length=2000, null=True, blank=True)  # sex life? previous marriages?
    relationships = models.CharField(max_length=2000, null=True, blank=True)
    employment = models.CharField(max_length=2000, null=True, blank=True)  # employment history and current job
    pets = models.CharField(max_length=2000, null=True, blank=True)

    # personality
    hopes_and_dreams = models.CharField(max_length=2000, null=True, blank=True)
    fears = models.CharField(max_length=2000, null=True, blank=True)
    hobbies = models.CharField(max_length=2000, null=True, blank=True)
    likes = models.CharField(max_length=2000, null=True, blank=True)
    dislikes = models.CharField(max_length=2000, null=True, blank=True)
    personality = models.CharField(max_length=2000, null=True, blank=True)

    # misc
    skills = models.CharField(max_length=3000, null=True, blank=True)  # skills? superpowers?
    weaknesses = models.CharField(max_length=3000, null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100, null=False)
