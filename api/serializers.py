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
    document = DocumentSerializer(read_only=True)
    label = LabelSerializer(read_only=True)
    document_id = serializers.PrimaryKeyRelatedField(queryset=Document.objects.all(), source='document', write_only=True)
    label_id = serializers.PrimaryKeyRelatedField(queryset=Label.objects.all(), source='label', write_only=True)
    class Meta:
        model = Annotation
        fields = ('id', 'document','document_id', 'start', 'end', 'label','label_id')

class AnnotationSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ('id', 'document', 'start', 'end', 'label')


