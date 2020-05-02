from rest_framework import permissions
from django_otp import user_has_device
from .utils import otp_user_is_verified

class IsOtpVerified(permissions.BasePermission):
    message = "You do not have a valid OTP"

    def has_permission(self, request, view):
        if user_has_device(request.user):
            return otp_user_is_verified(self,request)
        else:
            return True


class IsStaff(permissions.BasePermission):
    message = "Your account is not authorized to perform this action"

    def has_permission(self, request, view):
      return request.user.is_staff