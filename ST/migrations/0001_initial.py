# Generated by Django 3.0 on 2019-12-07 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latitude', models.FloatField(help_text='Latitude of sighting')),
                ('Longtitude', models.FloatField(help_text='Longtitude of sighting')),
                ('ID', models.CharField(help_text='Uniqueid of sighting', max_length=100)),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], max_length=3)),
                ('Date', models.DateField(help_text='sighting day')),
                ('Age', models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('?', '?')], max_length=10)),
                ('Primary_Fur_Color', models.CharField(choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], max_length=30)),
                ('LOCATION', models.CharField(choices=[('Ground Plane', 'Ground_Plane'), ('Above Ground', 'Above_Ground')], max_length=30)),
                ('Specific_location', models.CharField(max_length=100)),
                ('Running', models.BooleanField()),
                ('Chasing', models.BooleanField()),
                ('Climbing', models.BooleanField()),
                ('Eating', models.BooleanField()),
                ('Foraging', models.BooleanField()),
                ('Other_Activities', models.CharField(max_length=100)),
                ('Kuks', models.BooleanField()),
                ('Quaas', models.BooleanField()),
                ('Moans', models.BooleanField()),
                ('Tail_flags', models.BooleanField()),
                ('Tail_twitches', models.BooleanField()),
                ('Approaches', models.BooleanField()),
                ('Indifferent', models.BooleanField()),
                ('Runs_form', models.BooleanField()),
            ],
        ),
    ]