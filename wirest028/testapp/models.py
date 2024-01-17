from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    subject = models.CharField(max_length=64)

    def __str__(self):
        return self.first_name
    
class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books_by_author')
    release_date = models.DateField(max_length=64)
    rating = models.IntegerField()

    def __str__(self):
        return self.title

