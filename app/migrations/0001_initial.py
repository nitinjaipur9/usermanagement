# Generated by Django 5.0.7 on 2024-07-14 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile_photo', models.ImageField(upload_to='profile_photos/')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=28)),
                ('address', models.CharField(max_length=500)),
                ('user_type', models.CharField(choices=[('patient', 'Patient'), ('doctor', 'Doctor')], max_length=10)),
            ],
        ),
    ]