# Generated by Django 4.1.7 on 2023-03-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statsapp', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistika',
            name='sana',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]