from django.db import models
from RuntimeTerror import settings
from django.db.models.deletion import CASCADE

# Create your models here.

class Course(models.Model):
    User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(User, on_delete=CASCADE)
    joined_on = models.DateTimeField(auto_now=True)
    title = models.TextField(max_length=50)
    headline = models.TextField()
    course_duration = models.TextField(max_length=15)
