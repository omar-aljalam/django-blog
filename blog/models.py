from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

# Post Model # Title, Excerpt, Image Name, Date, Slug, Content, Author (Foreign Key), Tags (Many To Many Field)
class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, related_name="posts", null=True)
    tags = models.ManyToManyField("Tag")

# Author Model First Name, Last Name, Email # One To Many Relationship with Post
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()

    
# Tag Model # Caption # Many To Many Relationship with Post
class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption