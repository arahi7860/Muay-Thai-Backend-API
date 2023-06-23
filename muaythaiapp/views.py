from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from .models import Technique, TrainingDrill, Category
from .serializers import TechniqueSerializer, TrainingDrillSerializer, CategorySerializer
import json
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import JsonResponse
from django.db.models import ProtectedError
from .update_drill import update_drills_with_ids
from django.conf import settings

class TechniqueViewSet(viewsets.ModelViewSet):
    queryset = Technique.objects.all()
    serializer_class = TechniqueSerializer

    def create(self, request, *args, **kwargs):
        technique_data = request.data

        category_name = technique_data.get('category')

        # Check if the category already exists
        category, created = Category.objects.get_or_create(name=category_name)

        move_data = {
            'name': technique_data.get('name'),
            'description': technique_data.get('description'),
            'img': technique_data.get('img'),
            'category': category.id
        }

        # Create a serializer instance with the move data
        serializer = self.get_serializer(data=move_data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Save the technique instance
        technique_instance = serializer.save()

        # Update the category's moves in the CategoryViewSet
        category_viewset = CategoryViewSet()
        category_viewset.queryset = Category.objects.all()  # Set the queryset to retrieve all categories
        category_viewset.update_category_moves(category_name, technique_instance)

        return Response({"message": "Technique created successfully"}, status=status.HTTP_201_CREATED)


class TrainingDrillViewSet(viewsets.ModelViewSet):
    queryset = TrainingDrill.objects.all()
    serializer_class = TrainingDrillSerializer

    # Import statement added here
    from .update_drill import update_drills_with_ids

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        # Get all training drills
        training_drills = self.get_queryset()

        # Loop through each training drill and delete it along with the related techniques
        for drill in training_drills:
            drill.techniques.clear()
            drill.delete()

        # Call the update_drills_with_ids function
        update_drills_with_ids(training_drills)

        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryViewSet(viewsets.ViewSet):
    serializer_class = CategorySerializer

    def list(self, request):
        categories = Category.objects.all()
        serializer = self.serializer_class(categories, many=True, context={'include_techniques': True})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        category = get_object_or_404(Category, name=pk)
        serializer = self.serializer_class(category, context={'include_techniques': True})
        return Response(serializer.data)

    def update_category_moves(self, category_name, technique_instance):
        category = Category.objects.filter(name=category_name).first()
        if category:
            category.related_techniques.add(technique_instance)
