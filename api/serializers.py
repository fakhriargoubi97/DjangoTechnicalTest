# api/serializers.py
from rest_framework import serializers
from .models import Document, Label, Annotation

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'title', 'text')

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ('id', 'name', 'color')

class AnnotationSerializer(serializers.ModelSerializer):
    document:DocumentSerializer()
    label:LabelSerializer()
    class Meta:
        model = Annotation
        fields = ('id', 'document', 'start', 'end', 'label')


