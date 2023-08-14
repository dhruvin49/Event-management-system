from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


