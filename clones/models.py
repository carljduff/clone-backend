from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, null=True)
    address = models.CharField(max_length=500, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    isPublic = models.BooleanField(default=False)
    STATUS_CHOICES = (
        ('1', 'Ongoing'),
        ('2', 'Past Event'),
        ('3', 'Event Cancelled')
    )
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='1')
    guests = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='guests', blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img = models.ForeignKey('Photo', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    label = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.label

class Item(models.Model):
    label = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

class Post(models.Model):
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Photo(models.Model):
    img = models.ImageField(upload_to='clones/images/', blank=True, default='')

class CustomUser(AbstractUser):
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


