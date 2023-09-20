from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

POPTRENDS = (
    ('INC', 'Increading'),
    ('DEC', 'Decreasing'),
    ('UNK', 'Unknown')
)

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Sponsor(models.Model):
  name = models.CharField(max_length=50)
  age = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('sponsor_detail', kwargs={'pk': self.id})

class Finch(models.Model):

    species = models.CharField(max_length=150)
    population = models.IntegerField()
    habitat = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    population_trend = models.CharField(
        max_length=3,
        choices=POPTRENDS,
        default=POPTRENDS[2][0]
    )
    sponsors = models.ManyToManyField(Sponsor)

    def __str__(self):
        return f'{self.species} ({self.id})'
    
    def __str__ (self):
        return f'{self.get_population_trend_display()}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    finch = models.ForeignKey(
        Finch,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}" 
