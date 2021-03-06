# Generated by Django 3.0.8 on 2020-09-25 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='lessoncount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_number_of_lessons', models.IntegerField(blank=True, null=True)),
                ('number_of_lessons_available', models.IntegerField(blank=True, null=True)),
                ('recent_payment_status', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessoncount', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
