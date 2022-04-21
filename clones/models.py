from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(null=True)
    img = models.ImageField()
    address = models.ForeignKey('Address', on_delete= models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    isPublic = models.BooleanField(default=False)
    GOING = 1
    PAST = 2
    CANCELLED = 3
    STATUS_CHOICES = (
        (GOING, 'Ongoing'),
        (PAST, 'Past Event'),
        (CANCELLED, 'Event Cancelled')
    )
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=GOING)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

