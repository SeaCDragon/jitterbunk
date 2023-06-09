# Generated by Django 3.2 on 2023-06-07 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bunks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bunk',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='Bunks.user'),
        ),
        migrations.AlterField(
            model_name='bunk',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='Bunks.user'),
        ),
    ]
