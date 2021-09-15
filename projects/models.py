from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    style_id = models.OneToOneField('Style', on_delete=models.CASCADE, related_name='style')
    aria = models.PositiveSmallIntegerField()
    designer = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    preview = models.ImageField(upload_to='media/%Y/%m/%d')
    slug = models.SlugField(allow_unicode=True)
