from django.db import models

# Create your models here.
class Question(models.Model):
     question=models.CharField(max_length=20)
     pub_date=models.DateTimeField(auto_now=True)
class Chioce(models.Model):
    chioce=models.CharField(max_length=20)
    votes=models.IntegerField(default=0)
    name=models.ForeignKey(Question,on_delete=models.CASCADE)

