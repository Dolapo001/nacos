from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample, OpenApiParameter
from rest_framework import status


def login_docs():
    return extend_schema(
        summary="User Login",
        description=(
            """
            This endpoint allows a user to log in by providing valid credentials (username and password.
            """
        ),
        tags=['Authentication'],
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description="Login successful.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Success response",
                        value={"message": "Login successful"}
                    )
                ]
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                description="Invalid credentials.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Error response",
                        value={"error": "Invalid credentials"}
                    )
                ]
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                description="Internal server error.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Error response",
                        value={"error": "Internal server error"}
                    )
                ]
            )
        }
    )