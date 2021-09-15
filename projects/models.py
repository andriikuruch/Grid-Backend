from django.db import models
from cloudinary.models import CloudinaryField


class Project(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    # style_id = models.OneToOneField('Style', on_delete=models.CASCADE, related_name='style')
    aria = models.PositiveSmallIntegerField()
    designer = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    preview = CloudinaryField('image')
    slug = models.SlugField(allow_unicode=True)
