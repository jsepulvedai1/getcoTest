from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import User
from ..serializer import UserSerializer
from rest_framework.exceptions import ParseError
from rest_framework.permissions import AllowAny


class RegisterUser(APIView):

    permission_classes = (AllowAny,)

    def avaible_email(self, email):
        try:
            User.objects.get(email=email)
            return False
        except User.DoesNotExist:
            return True

    def post(self, request):
        if not request.data.get('email'):
            raise ParseError("email is required", code=400)
        if not self.avaible_email(request.data['email']):
            json_error = {
                "detail": "email already in use"
            }
            return Response(json_error, status=status.HTTP_403_FORBIDDEN)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
