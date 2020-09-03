from rest_framework.serializers import ModelSerializer
from .models import FileInfo,Status

class FileSerializer(ModelSerializer):
    class Meta():
        model = FileInfo
        fields = '__all__'


class StatusSerializer(ModelSerializer):
    class Meta():
        model = Status
        fields = '__all__'


