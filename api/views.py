from django.shortcuts import render

# api/views.py
from rest_framework import generics
from .models import Document, Label, Annotation
from .serializers import DocumentSerializer, LabelSerializer, AnnotationSerializer,AnnotationSerializerCreate

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

class AnnotationListView(generics.ListAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializerCreate

class AnnotationListCreateView(generics.ListCreateAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer

class AnnotationCreateView(generics.CreateAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializerCreate
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AnnotationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
