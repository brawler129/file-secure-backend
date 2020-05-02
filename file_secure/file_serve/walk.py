from os import listdir
from os.path import join,isdir,isfile,basename,splitext,getsize,getmtime
import time

path = "media/share_space";
def construct_file_tree(path):
    dict = {}
    if isdir(path):
        dict["name"] = basename(path)
        dict["extension"] = "folder"
        dict["isFolder"] = True
        dict["items"] = len(listdir(path))
        dict["absPath"] = path.split("/")[1]
        dict["lmt"] = time.strftime("%d-%m-%Y %H:%M",time.localtime(getmtime(path)))
        dict["children"] = [construct_file_tree(join(path,x)) for x in listdir(path)]
    elif isfile(path):
        dict["name"],dict["extension"]  =   splitext(basename(path))
        dict["isFolder"] = False
        dict["items"] = 0
        dict["absPath"] = path.split("/")[1]
        dict["size"] = round(getsize(path) /(1024 * 1024),3)
        dict["lmt"] = time.strftime("%d-%m-%Y %H:%M",time.localtime(getmtime(path)))
        dict["children"] = []
    return dict


def get_file_tree():
    return construct_file_tree(path)