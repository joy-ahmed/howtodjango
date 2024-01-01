from django.db import models
from django.contrib.auth.models import AbstractUser

USER_ROLE = (
    ('', '---Select account type---'),
    ('blogger', 'Blogger'),
    ('user', 'User'),
)

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='users/avatar/', blank=True, null=True, default='avatar.png')
    bio = models.TextField(blank=True, null=True, default="")
    user_role = models.CharField(max_length=10, choices=USER_ROLE)
