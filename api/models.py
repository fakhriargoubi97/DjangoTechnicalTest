from django.db import models

# api/models.py
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

class Label(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)


class Annotation(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    # document_id = models.IntegerField()
    # label_id = models.IntegerField()
    start = models.IntegerField()
    end = models.IntegerField()
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
