# Generated by Django 2.2.3 on 2019-07-18 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellfresh', '0008_order_allprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(null=True, on_delete=True, to='sellfresh.Address'),
        ),
        migrations.AddField(
            model_name='order',
            name='pay',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
