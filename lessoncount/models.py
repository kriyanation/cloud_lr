# Create your models here.
from django.db import models


class lessoncount(models.Model):
    user = models.ForeignKey('auth.User', related_name='lessoncount', on_delete=models.CASCADE)
    total_number_of_lessons = models.IntegerField(null=True,blank=True)
    number_of_lessons_available = models.IntegerField(null=True,blank=True)
    recent_payment_status = models.CharField(max_length=255,null=True,blank=True)
