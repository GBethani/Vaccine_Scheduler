from django.db import models
from drug.models import Drug

# Create your models here.
class Center(models.Model):
    name = models.CharField(max_length=124)
    address = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Storage(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    total_quantity = models.IntegerField(default=0)
    booked_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.center.name + " | " + self.drug.name
