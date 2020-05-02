from rest_framework import serializers
from .models import Rename, Create, Delete, Move, Download, Upload


class RenameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rename
        fields = '__all__'


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Create
        fields = '__all__'


class DeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delete
        fields = '__all__'


class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = '__all__'


class DownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Download
        fields = '__all__'


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = '__all__'
