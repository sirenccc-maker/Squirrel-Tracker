# Generated by Django 3.0 on 2019-12-07 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ST', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='squirrel',
            old_name='ID',
            new_name='Squirrel_ID',
        ),
    ]