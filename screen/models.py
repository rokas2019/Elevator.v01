from django.db import models
from django.utils import timezone


class Level(models.Model):
    class LevelName(models.IntegerChoices):
        PARKING = 0
        CUSTOMER_CARE = 1
        MARKETING_SALES = 2

    level = models.IntegerField(choices=LevelName.choices)
    image = models.ImageField(default='images/floor10.png', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return str(self.level)


class Screen(models.Model):
    current_floor_level = models.ForeignKey(Level, on_delete=models.RESTRICT)

    def __str__(self):
        return str(self.current_floor_level)


class Arrow(models.Model):
    UP = 'up'
    DOWN = 'down'
    DIRECTION_CHOICES = [
        (UP, 'Up'),
        (DOWN, 'Down'),
    ]

    direction = models.CharField(max_length=4, choices=DIRECTION_CHOICES)
    arrow_image = models.ImageField(default='images/arrow_up.gif', height_field=None, width_field=None, max_length=100)

    def get_direction_display(self):
        for choice in self.DIRECTION_CHOICES:
            if choice[0] == self.direction:
                return choice[1]
        return ''

    def __str__(self):
        return f"Arrow: {self.get_direction_display()}"


class CurrentTime(models.Model):
    time = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.time = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Current Time: {self.time.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"

