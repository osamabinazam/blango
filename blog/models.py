from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.utils import timezone

# Create your models here.

# Handle Comments on The Blog post Using Generic Relationship
class Comment(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

# Add Tags
class Tag(models.Model):
  value = models.TextField(max_length=100)

  # String Representation
  def __str__(self):
    return self.value

# Post Model
class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now =True)
  published_at = models.DateTimeField(blank=True, null=True)
  title = models.TextField(max_length=100)
  slug = models.SlugField()
  summary = models.TextField(max_length=500)
  content = models.TextField()
  tags = models.ManyToManyField(Tag, related_name="posts")

  # Generic Relation 
  comments = GenericRelation(Comment)

  # String Representation
  def __str__(self):
    return self.title 


