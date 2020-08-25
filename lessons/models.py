

# Create your models here.
from django.db import models
import uuid
from django.conf import settings


def user_lesson_title_image(instance,filename):
    split_list = filename.split(".")
    extension = ""
    if split_list is not None and split_list != "":
        extension = split_list[1]
        print(extension)
    return 'lessons/user_{0}/{1}/{2}/{3}'.format(instance.user.id,instance.class_id, instance.lesson_id,"title."+extension)

def user_lesson_directory(instance, filename):
    split_list = filename.split(".")
    extension = ""
    if split_list is not None and split_list != "":
        extension = split_list[1]
        print(extension)

    return 'lessons/user_{0}/{1}/{2}/{3}'.format(instance.user.id,instance.class_id, instance.lesson_id,"title."+extension)
def user_lesson_term1_image(instance,filename):
    split_list = filename.split(".")
    extension = ""
    if split_list is not None and split_list != "":
        extension = split_list[1]
        print(extension)
    return 'lessons/user_{0}/{1}/{2}/{3}'.format(instance.user.id, instance.class_id, instance.lesson_id,
                                                 "term1." + extension)
def user_lesson_term2_image(instance,filename):
    split_list = filename.split(".")
    extension = ""
    if split_list is not None and split_list != "":
        extension = split_list[1]
        print(extension)
    return 'lessons/user_{0}/{1}/{2}/{3}'.format(instance.user.id, instance.class_id, instance.lesson_id,
                                                 "term2." + extension)
def user_lesson_term3_image(instance,filename):
    split_list = filename.split(".")
    extension = ""
    if split_list is not None and split_list != "":
        extension = split_list[1]
        print(extension)
    return 'lessons/user_{0}/{1}/{2}/{3}'.format(instance.user.id, instance.class_id, instance.lesson_id,
                                                 "term3." + extension)
def user_lesson_step1_image(instance,filename):
    split_list = filename.split(".")
    extension = ""
    if split_list is not None and split_list != "":
        extension = split_list[1]
        print(extension)
    return 'lessons/user_{0}/{1}/{2}/{3}'.format(instance.user.id, instance.class_id, instance.lesson_id,
                                                 "step1." + extension)
def user_lesson_step2_image(instance,filename):
    split_list = filename.split(".")
    extension = ""
    if split_list is not None and split_list != "":
        extension = split_list[1]
        print(extension)
    return 'lessons/user_{0}/{1}/{2}/{3}'.format(instance.user.id, instance.class_id, instance.lesson_id,
                                                 "step2." + extension)
def user_lesson_step3_image(instance,filename):
    split_list = filename.split(".")
    extension = ""
    if split_list is not None and split_list != "":
        extension = split_list[1]
        print(extension)
    return 'lessons/user_{0}/{1}/{2}/{3}'.format(instance.user.id, instance.class_id, instance.lesson_id,
                                                 "step3." + extension)
def user_lesson_step4_image(instance,filename):
    split_list = filename.split(".")
    extension = ""
    if split_list is not None and split_list != "":
        extension = split_list[1]
        print(extension)
    return 'lessons/user_{0}/{1}/{2}/{3}'.format(instance.user.id, instance.class_id, instance.lesson_id,
                                                 "step4." + extension)
def user_lesson_step5_image(instance,filename):
    split_list = filename.split(".")
    extension = ""
    if split_list is not None and split_list != "":
        extension = split_list[1]
        print(extension)
    return 'lessons/user_{0}/{1}/{2}/{3}'.format(instance.user.id, instance.class_id, instance.lesson_id,
                                                 "step5." + extension)
def user_lesson_step6_image(instance,filename):
    split_list = filename.split(".")
    extension = ""
    if split_list is not None and split_list != "":
        extension = split_list[1]
        print(extension)
    return 'lessons/user_{0}/{1}/{2}/{3}'.format(instance.user.id, instance.class_id, instance.lesson_id,
                                                 "step6." + extension)
def user_lesson_step7_image(instance,filename):
    split_list = filename.split(".")
    extension = ""
    if split_list is not None and split_list != "":
        extension = split_list[1]
        print(extension)
    return 'lessons/user_{0}/{1}/{2}/{3}'.format(instance.user.id, instance.class_id, instance.lesson_id,
                                                 "step7." + extension)
def user_lesson_step8_image(instance,filename):
    split_list = filename.split(".")
    extension = ""
    if split_list is not None and split_list != "":
        extension = split_list[1]
        print(extension)
    return 'lessons/user_{0}/{1}/{2}/{3}'.format(instance.user.id, instance.class_id, instance.lesson_id,
                                                 "step8." + extension)

class lesson(models.Model):
    global_lesson_id = models.AutoField(primary_key=True)
    lesson_id = models.IntegerField()
    class_id = models.IntegerField()
    user = models.ForeignKey('auth.User', related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255,null=True,blank=True)
    title_image = models.FileField(upload_to = user_lesson_title_image, null=True,blank=True)
    title_video = models.FileField(upload_to = user_lesson_title_image, null=True,blank=True)
    title_description = models.TextField(null=True,blank=True)

    term1 = models.CharField(max_length=255,null=True,blank=True)
    term1_description = models.TextField(null=True, blank=True)
    term1_image = models.FileField(upload_to=user_lesson_term1_image, null=True, blank=True)

    term2 = models.CharField(max_length=255,null=True,blank=True)
    term2_description = models.TextField(null=True, blank=True)
    term2_image = models.FileField(upload_to=user_lesson_term2_image, null=True, blank=True)

    term3 = models.CharField(max_length=255, null=True, blank=True)
    term3_description = models.TextField(null=True, blank=True)
    term3_image = models.FileField(upload_to=user_lesson_term3_image, null=True, blank=True)

    number_of_steps = models.IntegerField(null=True,blank=True)
    step1_description = models.CharField(max_length=255,null=True,blank=True)
    step1_image = models.FileField(upload_to=user_lesson_step1_image, null=True, blank=True)

    step2_description = models.CharField(max_length=255,null=True,blank=True)
    step2_image = models.FileField(upload_to=user_lesson_step2_image, null=True, blank=True)

    step3_description = models.CharField(max_length=255, null=True, blank=True)
    step3_image = models.FileField(upload_to=user_lesson_step3_image, null=True, blank=True)

    step4_description = models.CharField(max_length=255, null=True, blank=True)
    step4_image = models.FileField(upload_to=user_lesson_step4_image, null=True, blank=True)

    step5_description = models.CharField(max_length=255, null=True, blank=True)
    step5_image = models.FileField(upload_to=user_lesson_step5_image, null=True, blank=True)

    step6_description = models.CharField(max_length=255, null=True, blank=True)
    step6_image = models.FileField(upload_to=user_lesson_step6_image, null=True, blank=True)

    step7_description = models.CharField(max_length=255, null=True, blank=True)
    step7_image = models.FileField(upload_to=user_lesson_step7_image, null=True, blank=True)

    step8_description = models.CharField(max_length=255, null=True, blank=True)
    step8_image = models.FileField(upload_to=user_lesson_step8_image, null=True, blank=True)

    questions = models.TextField(null=True, blank=True)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    #models.CharField(max_length=255)

    class Meta:
        constraints = [models.UniqueConstraint(fields = ['class_id','lesson_id','user'],name='unique-lesson')]



