from rest_framework import serializers

from .models import Famous



class FamousSerializer(serializers.ModelSerializer):
    class Meta:
        model = Famous
        fields = ('title', 'cat_id')
