from django.db import models
from datetime import datetime

available_years = []
for year in range(2000, (datetime.now().year + 5)):
    available_years.append((year, year))

class Profile(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
        
class Record(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField(choices=available_years, default=datetime.now().year)
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=2000)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name