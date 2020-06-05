# Generated by Django 2.2.3 on 2019-07-16 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_typeinfo_pic'),
        ('sellfresh', '0004_auto_20190716_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='goods',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.Goodsinfo'),
        ),
        migrations.AddField(
            model_name='comment',
            name='orderid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sellfresh.Order'),
        ),
    ]