import os
import shutil


def renameFile(path,filename,renameTo):
    os.rename( (path+filename),(path + renameTo))


def createFolder(path,folderName):
    os.mkdir(path + folderName)

def deleteFile(path,filename):
    file_path = path + filename
    if os.path.isdir(file_path):
        shutil.rmtree(file_path)
    else:
        os.remove(file_path)

def moveFile(path,filename,moveTo):
    shutil.move((path + filename) , (moveTo + '/' + filename))