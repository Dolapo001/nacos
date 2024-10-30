from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')  # Corrected to 'username' instead of 'email'
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError(_("Must include 'username' and 'password'."))

        # Authenticate user
        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(_("Invalid credentials."))

        if not user.is_active:
            raise serializers.ValidationError(_("User account is inactive."))

        # Add the authenticated user to the validated data
        data['user'] = user
        return data
