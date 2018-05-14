from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    image = models.ImageField(upload_to='news_photo', blank=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    post_date = models.DateField(auto_now_add=True, blank=True)
    sender = models.ForeignKey(User)

    def __str__(self):
        return self.title


class CompletedCourses(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Barbers(models.Model):
    image = models.ImageField(upload_to='barber_photo', default='default_barber.jpg')
    first_last_name = models.CharField(max_length=128)
    description = models.TextField()
    completed_courses = models.ManyToManyField(CompletedCourses)

    def __str__(self):
        return self.first_last_name


class SalonInfo(models.Model):
    image = models.ImageField(upload_to='salon_photo', null=True, blank=True)
    header = models.CharField(max_length=256)
    content = models.TextField()

    def __str__(self):
        return self.header


class PriceTable(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Products(models.Model):
    image = models.ImageField(upload_to='products_photos', null=True, blank=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    quantity = models.IntegerField(default=0)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.name
