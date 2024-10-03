from django.db import models


class Order(models.Model):
    objects = models.Manager()
    apartment_number = models.CharField(max_length=10)
    pet_name = models.CharField(max_length=50)
    pet_breed = models.CharField(max_length=50)
    walk_date = models.DateField()
    walk_time = models.TimeField()

    def __str__(self):
        return f"{self.pet_name} ({self.pet_breed}) - {self.walk_date} {self.walk_time}"
