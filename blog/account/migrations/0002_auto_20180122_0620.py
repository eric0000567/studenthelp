# Generated by Django 2.0.1 on 2018-01-21 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.IntegerField(choices=[(1, '男'), (2, '女')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]