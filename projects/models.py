from django.db import models


class Project(models.Model):
    thumbnail = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ProjectPhoto(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    project = models.ForeignKey(Project, default=0, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.description
