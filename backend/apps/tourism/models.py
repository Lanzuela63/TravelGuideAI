#apps/tourism/models.py
from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'tourism'

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100, blank=True)
    province = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class TouristSpot(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tourist_spots/', default='tourist_spots/default.jpg')
    is_featured = models.BooleanField(default=False)  # show on homepage
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tourist_spot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} review for {self.tourist_spot.name}'

class Gallery(models.Model):
    tourist_spot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'Image of {self.tourist_spot.name}'

class OperatingHour(models.Model):
    DAYS_OF_WEEK = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]
    tourist_spot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=3, choices=DAYS_OF_WEEK, default='Mon')
    open_time = models.TimeField()
    close_time = models.TimeField()


    def __str__(self):
        return f'{self.tourist_spot.name} - {self.day}'


class SavedSpot(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='saved_spots')
    spot = models.ForeignKey('TouristSpot', on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'spot')

class VisitedSpot(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='visited_spots')
    spot = models.ForeignKey('TouristSpot', on_delete=models.CASCADE)
    visited_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'spot')