from rest_framework import serializers
from .models import Technique, TrainingDrill

class TechniqueSerializer(serializers.ModelSerializer):
    category = serializers.CharField()  # Update field name to 'category'

    class Meta:
        model = Technique
        fields = ['name', 'description', 'img', 'category']


class TrainingDrillSerializer(serializers.ModelSerializer):
    techniques = TechniqueSerializer(many=True)

    class Meta:
        model = TrainingDrill
        fields = ['name', 'description', 'techniques', 'parent_drill']

    def create(self, validated_data):
        techniques_data = validated_data.pop('techniques')
        training_drill = TrainingDrill.objects.create(**validated_data)

        for technique_data in techniques_data:
            Technique.objects.create(**technique_data, trainingdrill=training_drill)

        return training_drill

# class CategorySerializer(serializers.Serializer):
#     name = serializers.CharField()
#     moves = serializers.SerializerMethodField()

#     def get_moves(self, category):
#         include_techniques = self.context.get('include_techniques', False)
#         if include_techniques:
#             return category.get('moves', [])
#         else:
#             return []
