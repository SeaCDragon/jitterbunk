# Generated by Django 3.2 on 2023-06-07 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('photo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Bunk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_user', models.CharField(max_length=200)),
                ('time', models.DateTimeField(verbose_name='Date:')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bunks.user')),
            ],
        ),
    ]
