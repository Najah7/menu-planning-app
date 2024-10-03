from django.contrib.auth import forms, models


class UserCreationForm(forms.UserCreationForm):
    class Meta:
        model = models.User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]
