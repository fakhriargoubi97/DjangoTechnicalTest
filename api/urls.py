# api/urls.py
from django.urls import path
from .views import DocumentListCreateView, LabelRetrieveUpdateDestroyView,LabelListCreateView, AnnotationListCreateView,DocumentRetrieveUpdateDestroyView,AnnotationRetrieveUpdateDestroyView

urlpatterns = [
    path('documents/', DocumentListCreateView.as_view(), name='document-list-create'),
    path('documents/<int:pk>/', DocumentRetrieveUpdateDestroyView.as_view(), name='document-retrieve-update-destroy'),
    path('labels/', LabelListCreateView.as_view(), name='label-list-create'),
    path('labels/<int:pk>/', LabelRetrieveUpdateDestroyView.as_view(), name='label-retrieve-update-destroy'),
    path('annotations/', AnnotationListCreateView.as_view(), name='annotation-list-create'),
    path('annotations/<int:pk>/', AnnotationRetrieveUpdateDestroyView.as_view(), name='annotation-retrieve-update-destroy'),
]
