# Generated by Django 2.1.7 on 2019-06-07 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20190605_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persons',
            name='Persons_role',
        ),
        migrations.AddField(
            model_name='submenu',
            name='url',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='submenu',
            name='orden',
            field=models.IntegerField(),
        ),
    ]
