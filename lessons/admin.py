from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.lesson)
class LessonAdmin(admin.ModelAdmin):
    pass