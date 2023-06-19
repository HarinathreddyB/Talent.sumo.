from rest_framework import serializers
from app.models import *

class NoteMS(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields='__all__'