from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def get_file_upload_path(instance,filename):
    final_path = instance.path + '/' + filename
    return final_path

class Record(models.Model):
    path = models.CharField(blank=False, max_length=200)
    # Folder name for create folder(File in this projects context is a file element consisting of both files and folders
    filename = models.CharField(blank=False, max_length=255)
    time = models.DateTimeField(default=timezone.now)
    username = models.CharField(null=False, blank=False, max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET(username), blank=False)

    class Meta:
        abstract = True


class Rename(Record):
    renameTo = models.CharField(max_length=255)


class Delete(Record):
    multiple = models.BooleanField(default=False)


class Move(Record):
    moveTo = models.CharField(max_length=255)


class Create(Record):
    private = models.BooleanField(default=False)


class Download(Record):
    multiple = models.BooleanField(default=False)


class Upload(Record):
    isFolder = models.BooleanField(default=False)
    file_path = models.FileField(upload_to=get_file_upload_path,default="../media/")


