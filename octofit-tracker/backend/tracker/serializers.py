from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', 'title', 'duration_minutes', 'date', 'created_at']

    def get_id(self, obj):
        # Ensure any ObjectId or pk-like id is represented as a string
        return str(obj.pk)
