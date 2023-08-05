from rest_framework import serializers
from .models import AccountsAPICustomUser

class AccountsAPICustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsAPICustomUser
        fields = ('id', 'email', 'username', 'password')
        extra_kwargs = {'password':{'write_only': True}}