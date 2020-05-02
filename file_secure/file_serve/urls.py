from django.urls import path
from .views import get_share_space_tree,TOTPCreateView,TOTPVerifyView,test_request
from django.views.generic.base import TemplateView

urlpatterns = [
    path('get_tree_structure',get_share_space_tree,name = "get_share_space"),
    path('totp/create',TOTPCreateView.as_view()),
    path('totp/login/<int:token>',TOTPVerifyView.as_view()),
]