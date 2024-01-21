from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.topic_name


class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    Author=models.CharField(max_length=100)
    def __str__(self):
        return self.Author
class review(models.Model):
    Name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    rating=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return int(self.rating)