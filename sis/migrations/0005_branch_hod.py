# Generated by Django 2.0.7 on 2018-10-09 02:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0004_course_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='hod',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
