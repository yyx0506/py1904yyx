# Generated by Django 2.2.3 on 2019-07-10 03:22

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190710_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artical',
            name='body',
            field=DjangoUeditor.models.UEditorField(),
        ),
        migrations.RemoveField(
            model_name='artical',
            name='tag',
        ),
        migrations.AddField(
            model_name='artical',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
