from django.db import models
from django.utils import timezone

class Sector(models.Model):
  name = models.CharField(max_length = 50, db_index = True)
  updated_at = models.DateTimeField(auto_now = True)

  class Meta:
    unique_together = ('name',)

class Market(models.Model):
  name = models.CharField(max_length = 50, db_index = True)
  updated_at = models.DateTimeField(auto_now = True)

  class Meta:
    unique_together = ('name',)

class Stock(models.Model):
  sector = models.ForeignKey(Sector, on_delete = models.CASCADE, related_name = 'stocks')
  market = models.ForeignKey(Market, on_delete = models.CASCADE, related_name = 'stocks')
  code = models.CharField(max_length = 10, db_index = True)
  name = models.TextField(max_length = 100)
  industry= models.TextField(max_length = 500)
  updated_at = models.DateTimeField(auto_now = True)
