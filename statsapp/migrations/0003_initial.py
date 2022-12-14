# Generated by Django 4.1.1 on 2022-10-14 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0005_remove_sotuvchi_user_sotuvchi_user'),
        ('asosiyapp', '0005_initial'),
        ('statsapp', '0002_delete_statistika'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdor', models.PositiveSmallIntegerField(default=1)),
                ('jami', models.PositiveSmallIntegerField()),
                ('tolandi', models.PositiveSmallIntegerField()),
                ('nasiya', models.PositiveSmallIntegerField(default=0)),
                ('mahsulot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='asosiyapp.mahsulot')),
                ('mijoz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='asosiyapp.mijoz')),
                ('sotuvchi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.sotuvchi')),
            ],
        ),
    ]
