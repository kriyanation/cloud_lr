# Generated by Django 3.0.8 on 2020-08-02 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_auto_20200802_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='global_lesson_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]