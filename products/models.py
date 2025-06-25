from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    
    

