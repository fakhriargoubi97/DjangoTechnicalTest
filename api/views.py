from django.shortcuts import render

# api/views.py
from rest_framework import generics
from .models import Document, Label, Annotation
from .serializers import DocumentSerializer, LabelSerializer, AnnotationSerializer

class DocumentListCreateView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class LabelListCreateView(generics.ListCreateAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

class LabelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

class AnnotationListCreateView(generics.ListCreateAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer

class AnnotationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
