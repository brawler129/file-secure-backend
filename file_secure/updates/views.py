from django.shortcuts import render
from django.utils.encoding import smart_str
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from file_serve.permissions import IsStaff, IsOtpVerified
from .serializers import RenameSerializer, CreateSerializer \
    , DeleteSerializer, MoveSerializer, DownloadSerializer, UploadSerializer
from .updates import renameFile, createFolder, deleteFile, moveFile
from django.contrib.auth.models import User
from .utils import create_record_object, fileExists
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from django.http import HttpResponse, FileResponse
import magic


def get_paths(base_path, filename):
    path = base_path + '/'
    file_path = path + filename
    return path, file_path


# PATH IS THE PATH OF THE DIRECTORY OF OPERATION AND FILENAME IS THE NAME OF THE FILE OPERATED UPON
# THIS IS DONE AS DIFFERENT APPLICATIONS REQUIRE DIFFERENTLY FORMATTED PATHS

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsStaff, IsOtpVerified])
def rename_file_view(request):
    if request.method == 'POST':
        record = create_record_object(data=request.data, user=request.user)
        record['renameTo'] = request.data['renameTo']
        path, file_path = get_paths(record['path'], record['filename'])
        rename_serializer = RenameSerializer(data=record)
        if rename_serializer.is_valid():
            if fileExists(file_path):
                renameFile(path, record['filename'], record['renameTo'])
                rename_serializer.save()
            else:
                return Response("Invalid path ", status=status.HTTP_400_BAD_REQUEST)
            return Response("File object successfully renamed", status=status.HTTP_200_OK)
        return Response(rename_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsStaff, IsOtpVerified])
def create_folder_view(request):
    if request.method == 'POST':
        record = create_record_object(data=request.data, user=request.user)
        path, file_path = get_paths(record['path'], record['filename'])
        create_serializer = CreateSerializer(data=record)
        if create_serializer.is_valid():
            createFolder(path, record['filename'])
            create_serializer.save()
            return Response("Successfully Created New Folder", status=status.HTTP_200_OK)
        else:
            return Response(create_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated,IsOtpVerified,IsStaff])
def delete_file_view(request):
    if request.method == 'POST':
        record = create_record_object(data=request.data, user=request.user)
        path, file_path = get_paths(record['path'], record['filename'])
        delete_serializer = DeleteSerializer(data=record)
        if fileExists(file_path):
            if delete_serializer.is_valid():
                deleteFile(path, record['filename'])
                delete_serializer.save()
                return Response("Successfully deleted item", status=status.HTTP_200_OK)
            else:
                return Response(delete_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Specified file or directory does not exits", status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsStaff, IsOtpVerified, IsAuthenticated])
def move_file_view(request):
    if request.method == 'POST':
        record = create_record_object(data=request.data, user=request.user)
        path, file_path = get_paths(record['path'], record['filename'])
        record['moveTo'] = request.data['moveTo']
        move_serializer = MoveSerializer(data=record)
        if fileExists(file_path):
            if move_serializer.is_valid():
                moveFile(path, record['filename'], record['moveTo'])
                move_serializer.save()
                return Response("Successfully moved file", status=status.HTTP_200_OK)
            else:
                return Response(move_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Specified file does not exits", status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsOtpVerified, IsAuthenticated])
def download_file_view(request):
    if request.method == 'POST':
        record = create_record_object(data=request.data, user=request.user)
        path, file_path = get_paths(record['path'], record['filename'])
        download_serializer = DownloadSerializer(data=record)
        mime_type = magic.from_file(file_path, mime=True)
        print(mime_type)
        print(smart_str(file_path))
        if fileExists(file_path):
            if download_serializer.is_valid():
                response = HttpResponse(open(file_path, 'rb'), content_type=mime_type)
                response['Content-Disposition'] = 'attachment;filename=%s' % record['filename']
                return response
            else:
                return Response(download_serializer.errors, status=status.HTTP_200_OK)
        else:
            return Response("Specified file does not exits", status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsOtpVerified, IsStaff])
@parser_classes([MultiPartParser])
def upload_file_view(request):
    if request.method == 'POST':
        print(request.data['username'])
        record = create_record_object(data=request.data, user=request.user)
        path, file_path = get_paths(record['path'], record['filename'])
        record['file_path'] = request.data['file']
        upload_serializer = UploadSerializer(data=record)
        if upload_serializer.is_valid():
            upload_serializer.save()
            return Response("Successfully Uploaded File", status=status.HTTP_200_OK)
        else:
            return Response(upload_serializer.errors,status=status.HTTP_400_BAD_REQUEST)





