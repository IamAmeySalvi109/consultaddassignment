# Generated by Django 2.2 on 2019-09-09 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]