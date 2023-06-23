from django.db import models

class Technique(models.Model):
    name = models.CharField(max_length=100, default='Untitled')
    description = models.TextField(default='No description provided')
    img = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=100, default='Default Category')

    def __str__(self):
        return self.name

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
