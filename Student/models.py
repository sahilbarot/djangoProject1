from django.db import models

# Create your models here.
class info(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=100)
    div = models.CharField(max_length=100)

    def __str__(self):
       return self.roll_no + "-" + self.div + "-" + self.name
