from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from .models import Technique, TrainingDrill
from .serializers import TechniqueSerializer, TrainingDrillSerializer
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

        move_data = {
            'name': technique_data.get('name'),
            'description': technique_data.get('description'),
            'img': technique_data.get('img'),
            'category': category_name  # Include category in move_data
        }

        print("Received data:", move_data)  # Print the received data

        serializer = self.get_serializer(data=move_data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        technique_instance = serializer.save()

        # Retrieve the updated data using the serializer
        updated_data = TechniqueSerializer(technique_instance).data

        # Return the updated data in the response
        return Response(updated_data, status=status.HTTP_201_CREATED)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        technique_instance = serializer.save()

        # Retrieve the updated data using the serializer
        updated_data = TechniqueSerializer(technique_instance).data

        # Return the updated data in the response
        return Response(updated_data, status=status.HTTP_200_OK)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Technique deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=False, methods=['post'])
    def create_technique(self, request):
        technique_data = request.data

        category_name = technique_data.get('category')

        move_data = {
            'name': technique_data.get('name'),
            'description': technique_data.get('description'),
            'img': technique_data.get('img'),
            'category': category_name  # Include category in move_data
        }

        print("Received data:", move_data)  # Print the received data

        serializer = self.get_serializer(data=move_data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        technique_instance = serializer.save()

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


