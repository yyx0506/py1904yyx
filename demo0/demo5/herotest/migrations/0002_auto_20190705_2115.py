# Generated by Django 2.2.3 on 2019-07-05 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herotest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='gender',
            field=models.CharField(choices=[('man', '男'), ('woman', '女')], default='man', max_length=20),
        ),
    ]
