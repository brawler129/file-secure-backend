from django.urls import path
from .views import rename_file_view,create_folder_view,delete_file_view,move_file_view,download_file_view, \
    upload_file_view


urlpatterns = [
    path('rename', rename_file_view),
    path('delete', delete_file_view),
    path('create_folder', create_folder_view),
    path('move', move_file_view),
    path('download', download_file_view),
    path('upload', upload_file_view)

]