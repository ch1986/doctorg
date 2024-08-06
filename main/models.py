from django.db import models
from django.utils import timezone

class Query(models.Model):
    age = models.PositiveSmallIntegerField(null=True)
    gender = models.CharField(null=True, max_length=20)
    symptoms = models.CharField(null=True, max_length=500)
    history = models.CharField(null=True, max_length=500)
    family = models.CharField(null=True, max_length=500)
    lifestyle = models.CharField(null=True, max_length=500)
    tests = models.CharField(null=True, max_length=500)
    other = models.CharField(null=True, max_length=500)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a query."""
        date = timezone.localtime(self.log_date)
        return f"'{self.age}' '{self.gender}' '{self.symptoms}' '{self.history}' '{self.family}' '{self.lifestyle}' '{self.tests}' '{self.other}'  logged on {date.strftime('%A, %d %B, %Y at %X')}"
