from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=56)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=56)

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    title = models.CharField(max_length=56)
    description = models.CharField(max_length=256, null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}: {self.description}'   