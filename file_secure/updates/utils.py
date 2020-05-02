import os


def create_record_object(data, user):
    record = {}
    record['path'] = data['path']
    record['filename'] = data['filename']
    record['username'] = data['username']
    record['user'] = user.pk
    return record


def fileExists(path):
    return os.path.isfile(path) or os.path.isdir(path)

