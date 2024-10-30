import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .docs import login_docs
from .serializers import LoginSerializer

# Configure logger
logger = logging.getLogger(__name__)


class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    @login_docs()
    def post(self, request, **kwargs):
        try:
            logger.info("Received login request data.")
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                user = serializer.validated_data.get('user')

                # Generate JWT tokens
                refresh = RefreshToken.for_user(user)
                access = refresh.access_token

                return Response({
                    'refresh': str(refresh),
                    'access': str(access),
                }, status=status.HTTP_200_OK)

            logger.error(f"Validation errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error(f"Error occurred during user login: {e}")
            return Response({'message': 'Internal Server Error', 'data': None},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
