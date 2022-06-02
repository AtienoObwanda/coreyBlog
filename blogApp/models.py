from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Models
class posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # keeps added date, default is used when you wat to be able to use lastEdited date 
    author = models.ForeignKey(User, on_delete=models.CASCADE) # If a user is deleted, their posts get deleted. 