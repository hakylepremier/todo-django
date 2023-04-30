from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=255)
  
  class Meta:
    verbose_name_plural = 'Categories'
  
  def __str__(self):
    return self.name
     
class Todo(models.Model):
  category = models.ForeignKey(Category, related_name="todos", on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  description = models.TextField(null=True, blank=True)
  isChecked = models.BooleanField(default=False)
  created_by = models.ForeignKey(User, related_name="todos", on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f'{self.name}. Category: {self.category}, Done: {self.isChecked}'
  
  
  