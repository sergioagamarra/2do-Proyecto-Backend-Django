from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

# Create your models here.
class EmailBackEnd(BaseBackend):
    def authenticate(self, request, username=None, email=None, password=None, **kwargs):
        User = get_user_model()

        if username is not None:

            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    return user
                else:
                    return None
            except User.DoesNotExist:
                return None

        else:
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    return user
                else:
                    return None
            except User.DoesNotExist:
                return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
