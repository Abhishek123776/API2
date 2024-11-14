from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    roll=serializers.IntegerField()
    name=serializers.CharField(max_length=50)
    marks=serializers.FloatField()