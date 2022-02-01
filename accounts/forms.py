from django.contrib.auth import get_user_model

# check for unique email and username

User = get_user_model()


class LoginForm(forms.Form):
    pass
