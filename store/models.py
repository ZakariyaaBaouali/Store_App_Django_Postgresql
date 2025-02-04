from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=50 , unique=True)
    user_profile_url = models.TextField()
    user_hash_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

