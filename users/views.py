from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer

# Create your views here.
class Register(APIView):
    # No permission restrictions; open endpoint (e.g., for registration)
    permission_classes = []

    def post(self, request):
        # Instantiate the serializer with incoming request data
        serializer = RegisterSerializer(data=request.data)

        try:
            # Validate the data (calls serializer.validate() and field-level validation)
            # Raises a ValidationError if data is invalid
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            print(e.detail)
            return Response (e.detail, status=400)

        # Save the validated data (calls serializer.create() under the hood)
        user = serializer.save()
        print(user)

        # Create or get a token for the newly created user
        token, _ = Token.objects.get_or_create(user=user)

        # Return the token and email in the response
        return Response({'token': token.key, 'email': user.email, 'name': user.name}, status=201)

class Login(APIView):
    permission_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        # print(vars(user))

        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key, 'email': user.email, 'name': user.name}, status=200)