from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=12)
    descriptions = models.TextField(null=True,blank=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt  = models.DateTimeField(auto_now_add=True)
  

    def __str__(self):
        return self.title


        