from django.db import models

# Create your models here.

# Author Database


class Author(models.Model):

    name = models.CharField(max_length=100, null=True)
    occupation = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    Author_Id = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    quotes = models.CharField(max_length=500, null=True)
    type_quotes = models.CharField(max_length=50, null=True)


class spcl_type(models.Model):
    catagories = models.CharField(max_length=5000, null=True)
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.catagories


class SpecialMessages(models.Model):
    quotes_type = models.ForeignKey(
        spcl_type, null=True, on_delete=models.SET_NULL)
    quotes = models.CharField(max_length=5000, null=True)
    sub_type = models.CharField(max_length=5000, null=True)
