from django.db import models
from django.contrib.auth.models import User

class Technique(models.Model):
    name = models.CharField(max_length=100, default='Untitled')
    description = models.TextField(default='No description provided')
    img = models.URLField(null=True, blank=True)
    categories = models.ManyToManyField('Category', related_name='related_techniques')

class TrainingDrill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    techniques = models.ManyToManyField(Technique)
    sequence = models.PositiveIntegerField(default=0)
    parent_drill = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='sub_drills')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['sequence']

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    techniques = models.ManyToManyField('Technique', related_name='related_categories')

    def __str__(self):
        return self.name or ''
