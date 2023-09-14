from django.db import models

POPTRENDS = (
    ('INC', 'Increading'),
    ('DEC', 'Decreasing'),
    ('UNK', 'Unknown')
)

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


    def __str__(self):
        return f'{self.species} ({self.id})'