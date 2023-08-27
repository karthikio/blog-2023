from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()

# Tag class 
class Tag(models.Model):
  name = models.CharField(max_length=100, unique=True, null=True)
  image = models.ImageField(blank=True, null=True, upload_to='uploads/tag/images/')
  slug = models.SlugField(null=True, blank=True)

  def save(self, *args, **kwargs):
    self.name = self.name.lower()
    if self.slug is None: 
      self.slug = slugify(self.name)
    super().save(*args, **kwargs)

  def __str__(self):
    return str(self.name)


# Post class
class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=200, unique=True)
  info = models.TextField(max_length=300)
  body = models.TextField(max_length=4000)
  image = models.ImageField(upload_to='uploads/post/images/%Y/%m', null=True, blank=True)
  created = models.DateField(auto_now_add=True, auto_now=False)
  slug = models.SlugField(null=True, blank=True)
  tag = models.ManyToManyField(Tag)
  featured = models.BooleanField(default=False)

  def save(self, *args, **kwargs):
    if self.slug is None: 
      self.slug = slugify(self.title)
    super().save(*args, **kwargs)

  def __str__(self):
    return str(self.title)


class Feedback(models.Model):
  name = models.CharField(max_length=100)
  content = models.TextField(max_length=500)