# Generated by Django 2.2.4 on 2019-08-25 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walk_of_fame', '0004_record_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='description',
            field=models.CharField(default='', max_length=2000),
            preserve_default=False,
        ),
    ]
