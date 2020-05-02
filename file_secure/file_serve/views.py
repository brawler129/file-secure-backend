from rest_framework.response import Response
from rest_framework import status,views
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import FolderTreeSerializer
from .walk import get_file_tree
from django_otp import devices_for_user
from django_otp.plugins.otp_totp.models import TOTPDevice
from .utils import get_custom_jwt
from .permissions import IsOtpVerified,IsStaff


def get_user_totp_device(self,user,confirmed = None):
    devices = devices_for_user(user,confirmed = confirmed)
    for device in devices:
        if isinstance(device,TOTPDevice):
            print("yes")
            return device

class TOTPCreateView(views.APIView):
    permission_classes = [IsAuthenticated,]

    def get(self,request,format = None):
        user = request.user
        device = get_user_totp_device(self,user)
        if not device:
            device = user.totpdevice_set.create(confirmed = False)
        url = device.config_url
        return Response(url,status=status.HTTP_201_CREATED)


class TOTPVerifyView(views.APIView):
    permission_classes = [IsAuthenticated,]

    def post(self,request,token,format=None):
        user = request.user
        device = get_user_totp_device(self,user)
        isVerified = bool(device.verify_token(token)) and bool(device);
        print(isVerified)
        if isVerified:
            if not device.confirmed:
                device.confirmed = True
                device.save()
            token = get_custom_jwt(user,device)
            return Response({'token':token}, status=status.HTTP_200_OK)

        return Response({'non_field_errors' : 'Invalid OTP'},status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated,IsOtpVerified])
def get_share_space_tree(request):

    if request.method == 'GET':
        file_tree = get_file_tree()
        serializer = FolderTreeSerializer(data=file_tree)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated,IsOtpVerified,IsStaff])
def test_request(request):

    if request.method == 'GET':
        return Response("This should only be accessable to staffs")