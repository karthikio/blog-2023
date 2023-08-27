# Generated by Django 3.2 on 2023-01-22 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='info',
            field=models.TextField(default='enter data', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
