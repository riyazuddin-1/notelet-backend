from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import SendSerializer
from .utils import generate_otp, send_otp

# Create your views here.
@api_view(["POST"])
@permission_classes([AllowAny])
def SendOTP(request):
    serializer = SendSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)

    email = serializer.validated_data["email"]

    verification_code = generate_otp()

    send_otp(email, verification_code)

    serializer.validated_data['verification_code'] = verification_code
    serializer.save()

    return Response({"success": True}, status=200)