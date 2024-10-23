from django.db import models


class Medicine(models.Model):
    brand_id = models.IntegerField()
    brand_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    genric = models.CharField(max_length=255)
    strength = models.CharField(max_length=255)
    manufacturers = models.CharField(max_length=255)
    package_container = models.CharField(max_length=255)
    package_size = models.CharField(max_length=255)

    def __str__(self):
        return self.brand_name
