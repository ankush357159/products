# Generated by Django 4.0.4 on 2022-06-03 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyPet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('breed', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('weight', models.IntegerField()),
                ('photo', models.ImageField(upload_to='pets/')),
            ],
        ),
    ]
