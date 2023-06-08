from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)

class Bunk(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    time = models.DateTimeField('Date:')