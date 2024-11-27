from django.db import models


class Students(models.Model):
  id = models.CharField(max_length=10,primary_key=True)
  pw = models.CharField(max_length=10)
  name = models.CharField(max_length=50)
  nicname = models.CharField(max_length=50)
  gender = models.CharField(max_length=10,default='Man')

  def __str__(self):
    return f"{self.id},{self.name},{self.nicname},{self.gender}"