# Generated by Django 2.2.4 on 2019-08-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walk_of_fame', '0002_auto_20190811_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='year',
            field=models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], default=2019),
        ),
    ]
