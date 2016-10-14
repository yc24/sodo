from django.db import models

class User(models.Model):
    nom_user = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
