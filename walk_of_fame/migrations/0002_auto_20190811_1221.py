# Generated by Django 2.2.4 on 2019-08-11 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walk_of_fame', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='LogMessage',
        ),
    ]
