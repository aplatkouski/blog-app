# Generated by Django 3.0.3 on 2020-02-28 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approved_comment',
            new_name='is_approved',
        ),
    ]
