import uuid

from django.db import models
from cloudinary.models import CloudinaryField


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=250)
    description = models.TextField()
    style_id = models.ForeignKey('Style', on_delete=models.CASCADE, related_name='styles')
    aria = models.PositiveSmallIntegerField()
    designer = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    preview = CloudinaryField('image')

    def __str__(self):
        return self.name


class Style(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=150)
    description = models.TextField()
    preview = CloudinaryField('image')

    def __str__(self):
        return self.name
