from django.db import models
from django.utils import timezone

class VS1H1(models.Model):
    Log_Time = models.DateTimeField(default=timezone.now)
    Stakeholder_Name = models.CharField(max_length=100)
    Wake_up_time = models.DateTimeField(default=timezone.now)
    Caffiene_Intake = models.CharField(max_length=100)
    Exercise_Description = models.CharField(max_length=200)
    Routine_Description = models.CharField(max_length=1000)
    Review_Intentions = models.CharField(max_length=300)
    Intended_Methods = models.CharField(max_length=1000)
    Session_Duration = models.DateTimeField(max_length=1000)
    Integrate_Awakening = models.CharField(max_length=1000)

    def __str__(self):
        return "%s %s"%(self.Log_Time, self.Stakeholder_Name,
        self.Wake_up_time, self.Caffiene_Intake, self.Exercise_Description,
        self.Routine_Description, self.Review_Intentions, self.Intended_Methods,
        self.Session_Duration, self.Integrate_Awakening)
