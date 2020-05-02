from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField


class FolderTreeSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=30)
    extension = serializers.CharField(allow_null=False, allow_blank=True, max_length=20, default=".unknown")
    isFolder = serializers.BooleanField(required=True, allow_null=False)
    items = serializers.IntegerField(required=True)
    absPath = serializers.CharField(required=True)
    size = serializers.FloatField(required=False)
    lmt = serializers.CharField(required=False)
    children = serializers.ListField(child=RecursiveField())
