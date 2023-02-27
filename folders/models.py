from django.db import models
from characters.models import Character
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Folder(models.Model):
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", null=True, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=100, null=False)
    created = models.TimeField(auto_created=True, default=timezone.now)

    def __str__(self):
        return self.name

# a character can belong to multiple folders
# express relationship as another table
class ContainedIn(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)