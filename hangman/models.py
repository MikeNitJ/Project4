from django.db import models

# Create your models here.
class Scoreboard(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(max_length=100)

    def __str__(self):
        return self.name, self.score
    
