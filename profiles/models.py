from django.db import models


class Profile(models.Model):
    content = models.TextField(null=True, blank=True)
