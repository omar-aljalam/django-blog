from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street}, {self.zip_code}"
    
    class Meta:
        # Register special names for the admin interface
        verbose_name_plural = "Address Entries"
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        null=True
    )

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
        )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True) # when an author is deleted, all their books are also deleted
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True) # db_index Saves the data in a way that makes searching easier, better performance, only use db_index for fields that will be searched frequently

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) # Harry Potter 1 -> harry-potter-1
        super().save(*args, **kwargs) 
    
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    def __str__(self):
        return f"{self.title} ({self.rating})"