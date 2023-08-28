from django.db import models
# Create your models here.

class SearchForm(models.Model): 
    word = models.CharField(max_length = 200)