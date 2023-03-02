from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Folder(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    created = models.TimeField(auto_created=True, default=timezone.now)
    private = models.BooleanField(null=False, default=False)  # whether other people can view this folder

    def __str__(self):
        return self.name
    
class RootFolder(Folder):
    root_owner = models.OneToOneField(User, on_delete=models.CASCADE)
    