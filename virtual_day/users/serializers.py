from rest_framework import serializers
from virtual_day.authentication import get_token
from virtual_day.users.models import User
from virtual_day.utils.exceptions import CommonException, PreconditionFailedException
from datetime import datetime
from virtual_day.utils import constants, messages, codes
from virtual_day.utils.validators import validate_password, validate_phone_number, validate_login
from django.contrib.auth.base_user import BaseUserManager
from virtual_day.business_service.send_email_service import send_email
from virtual_day.utils.decorators import query_debugger


class RegisterSerializer(serializers.ModelSerializer):
    """ Serializer for registration """

    class Meta:
        model = User
        fields = ('id', 'email', 'login', 'phone')

    @query_debugger
    def register(self, validated_data):
        """ Register new user """
        validate_phone_number(validated_data.get("phone"))
        email = validated_data.get("email")
        login = validate_login(validated_data.get("login"))

        password = BaseUserManager.make_random_password(self)
        manager = User.objects.create(login=login, email=email, role=constants.STUDENT)
        manager.set_password(password)
        manager.save()
        send_email(manager.login, manager.email, password)
        return manager


class UserSerializer(serializers.ModelSerializer):
    """ Manager Serializer in both console """

    class Meta:
        model = User
        fields = ('id', 'login', 'email', 'role')


class ChangePasswordSerializer(serializers.Serializer):
    """ change password for manager in both console """
    password = serializers.CharField()
    password_confirm = serializers.CharField()

    def validate(self, attrs):
        """ check if passwords are equal """
        password = validate_password(attrs['password'])
        password_confirm = validate_password(attrs['password'])
        if password != password_confirm:
            raise CommonException(code=codes.VALIDATION_ERROR, detail=messages.PASSWORD_NOT_EQUAL)
        return attrs

    def change(self):
        user = self.context['user']
        user.set_password(self.validated_data['password'])
        user.save()
        return user


class EnterEmailSerializer(serializers.Serializer):
    """ change email for manager in both console """
    email = serializers.EmailField()

    def validate(self, attrs):
        """ validate the email if email already exist in database """
        if User.objects.filter(email=attrs['email']).exclude(id=self.context['user'].id).count() > 0:
            raise CommonException(code=codes.ALREADY_EXISTS, detail=messages.EMAIL_ALREADY_EXISTS)
        return attrs

    @query_debugger
    def update_email(self):
        """ method get User and update his email """
        manager = User.objects.get(id=self.context['user'].id)
        manager.email = self.validated_data['email']
        manager.save()
        return manager


class LoginSerializer(serializers.Serializer):
    """ Login for manager in both console """
    login = serializers.CharField()
    password = serializers.CharField()

    @query_debugger
    def user_login(self):
        """ after login check device and create new object in model ManagerDevice
            (for each device generate new token) """
        try:
            user = User.objects.get(login=self.validated_data['login'])
            if not user.check_password(self.validated_data['password']):
                raise PreconditionFailedException(detail={"password": messages.WRONG_LOGIN_OR_PASSWORD},
                                                  code=codes.AUTH_ERROR)
        except User.DoesNotExist:
            raise PreconditionFailedException(detail={"password": messages.WRONG_LOGIN_OR_PASSWORD},
                                              code=codes.AUTH_ERROR)

        token = get_token(user)
        user.last_login = datetime.now()
        user.save()
        return token, user.role
