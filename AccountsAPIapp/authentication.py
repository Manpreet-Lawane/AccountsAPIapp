from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailAuthenticationBackend(ModelBackend):
    def authenticate(self, email=None, password=None, **kwargs):
        try:
            print('authentication.py', User)
            user = User.objects.filter(email=email).first()
            print('authentication.py', user)
            print(user if user else None)

            if user.check_password(password):
                return user
            return None
        except:
            return None

