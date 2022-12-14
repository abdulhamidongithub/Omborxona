# Generated by Django 4.1.1 on 2022-10-10 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0003_initial'),
        ('asosiyapp', '0004_remove_mahsulot_ombor_delete_client_delete_mahsulot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mijoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('nom', models.CharField(max_length=30)),
                ('manzil', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=30)),
                ('qarz', models.PositiveSmallIntegerField(default=0)),
                ('sotuvchi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.sotuvchi')),
            ],
        ),
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('brend', models.CharField(max_length=50)),
                ('miqdor', models.PositiveIntegerField()),
                ('narx', models.PositiveIntegerField()),
                ('olchov', models.CharField(max_length=30)),
                ('kelgan_sana', models.DateTimeField(auto_now_add=True)),
                ('sotuvchi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.sotuvchi')),
            ],
        ),
    ]
