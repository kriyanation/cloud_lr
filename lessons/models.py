

# Create your models here.
from django.db import models
import uuid
from django.conf import settings


def user_lesson_directory(instance,filename):
    return 'lessons/user_{0}/{1}/{2}/{3}'.format(instance.user.id,instance.class_id, instance.lesson_id,filename)

class lesson(models.Model):
    global_lesson_id = models.AutoField(primary_key=True)
    lesson_id = models.IntegerField()
    class_id = models.IntegerField()
    user = models.ForeignKey('auth.User', related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255,null=True,blank=True)
    title_image = models.FileField(upload_to = user_lesson_directory, null=True,blank=True)
    title_video = models.FileField(upload_to = user_lesson_directory, null=True,blank=True)
    title_description = models.TextField(null=True,blank=True)

    term1 = models.CharField(max_length=255,null=True,blank=True)
    term1_description = models.TextField(null=True, blank=True)
    term1_image = models.FileField(upload_to=user_lesson_directory, null=True, blank=True)

    term2 = models.CharField(max_length=255,null=True,blank=True)
    term2_description = models.TextField(null=True, blank=True)
    term2_image = models.FileField(upload_to=user_lesson_directory, null=True, blank=True)

    term3 = models.CharField(max_length=255, null=True, blank=True)
    term3_description = models.TextField(null=True, blank=True)
    term3_image = models.FileField(upload_to=user_lesson_directory, null=True, blank=True)

    number_of_steps = models.IntegerField(null=True,blank=True)
    step1_description = models.CharField(max_length=255,null=True,blank=True)
    step1_image = models.FileField(upload_to=user_lesson_directory, null=True, blank=True)

    step2_description = models.CharField(max_length=255,null=True,blank=True)
    step2_image = models.FileField(upload_to=user_lesson_directory, null=True, blank=True)

    step3_description = models.CharField(max_length=255, null=True, blank=True)
    step3_image = models.FileField(upload_to=user_lesson_directory, null=True, blank=True)

    step4_description = models.CharField(max_length=255, null=True, blank=True)
    step4_image = models.FileField(upload_to=user_lesson_directory, null=True, blank=True)

    step5_description = models.CharField(max_length=255, null=True, blank=True)
    step5_image = models.FileField(upload_to=user_lesson_directory, null=True, blank=True)

    step6_description = models.CharField(max_length=255, null=True, blank=True)
    step6_image = models.FileField(upload_to=user_lesson_directory, null=True, blank=True)

    step7_description = models.CharField(max_length=255, null=True, blank=True)
    step7_image = models.FileField(upload_to=user_lesson_directory, null=True, blank=True)

    step8_description = models.CharField(max_length=255, null=True, blank=True)
    step8_image = models.FileField(upload_to=user_lesson_directory, null=True, blank=True)

    questions = models.TextField(null=True, blank=True)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    #models.CharField(max_length=255)

    class Meta:
        constraints = [models.UniqueConstraint(fields = ['class_id','lesson_id','user'],name='unique-lesson')]



