from django.shortcuts import render
from rest_framework import viewsets
from .models import Technique, TrainingDrill, Category
from .serializers import TechniqueSerializer, TrainingDrillSerializer, CategorySerializer
import json
from rest_framework.response import Response
from rest_framework import status
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

        # Print the technique_data variable to inspect its contents
        print("technique_data:", technique_data)

        category_name = technique_data.get('category')

        # Check if the category already exists
        category, created = Category.objects.get_or_create(name=category_name)

        move_data = {
            'name': technique_data.get('name'),
            'description': technique_data.get('description'),
            'img': technique_data.get('img'),
            'categories': [category.id]  # Use 'categories' instead of 'category'
        }

        # Create a serializer instance with the move data
        serializer = self.get_serializer(data=move_data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Save the technique instance
        technique_instance = serializer.save()

        # Update the JSON file with the new technique data
        try:
            with open('techniques.json', 'r') as f:
                data = json.load(f)

            categories = data.get('categories', [])

            # Find the category with the specified name
            category = next((c for c in categories if c['name'] == category_name), None)

            if category:
                # Add the new technique to the category's moves
                category['moves'].append({
                    'name': technique_instance.name,
                    'description': technique_instance.description,
                    'img': technique_instance.img
                })

                # Update the JSON file with the modified data
                with open('techniques.json', 'w') as f:
                    json.dump(data, f, indent=4)

        except FileNotFoundError:
            return Response({'message': 'Data file not found.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"message": "Technique created successfully"}, status=status.HTTP_201_CREATED)


    def clear_techniques(self, request):
        category_name = request.data.get('category')

        # Find the category instance based on the name
        try:
            category_instance = Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            return Response({'message': f'Category "{category_name}" does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        # Delete the techniques belonging to the category
        deleted_count, _ = Technique.objects.filter(category=category_instance).delete()

        # Update the JSON file with the modified data
        try:
            with open('techniques.json', 'r') as f:
                data = json.load(f)

            categories = data.get('categories', [])

            # Find the category with the specified name
            category = next((c for c in categories if c['name'] == category_name), None)

            if category:
                # Remove all moves in the category
                category['moves'] = []

                # Update the JSON file with the modified data
                with open('techniques.json', 'w') as f:
                    json.dump(data, f, indent=4)

        except FileNotFoundError:
            return Response({'message': 'Data file not found.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'message': f'{deleted_count} technique(s) deleted successfully.'}, status=status.HTTP_200_OK)

    def create_technique(self, request):
        data = request.data

        name = data.get('name')
        description = data.get('description')
        img = data.get('img')
        category_name = data.get('category')

        # Perform further processing or validation as needed

        return Response


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
        with open('techniques.json', 'r') as f:
            data = json.load(f)

        categories = data.get('categories', [])
        serializer = self.serializer_class(categories, many=True, context={'include_techniques': True})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        with open('techniques.json', 'r') as f:
            data = json.load(f)

        categories = data['categories']
        category = next((c for c in categories if c['name'] == pk), None)
        if category:
            serializer = self.serializer_class(category, context={'include_techniques': True})
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
