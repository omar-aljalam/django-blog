from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
        )
    author = models.CharField(max_length=100, default="Uknown Author")
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True) # db_index Saves the data in a way that makes searching easier, better performance, only use db_index for fields that will be searched frequently

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) # Harry Potter 1 -> harry-potter-1
        super().save(*args, **kwargs) 
    
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    def __str__(self):
        return f"{self.title} ({self.rating})"