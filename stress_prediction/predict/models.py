from django.db import models
from django.contrib.auth.models import User

class StressPrediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    snoring_rate = models.FloatField()
    respiratory_rate = models.FloatField()
    body_temperature = models.FloatField()
    limb_movement = models.FloatField()
    blood_oxygen = models.FloatField()
    eye_movement = models.FloatField()
    sleep_hours = models.FloatField()
    heart_rate = models.FloatField()
    prediction_result = models.CharField(max_length=20)  # 'Stressed' or 'Not Stressed'
    prediction_date = models.DateTimeField(auto_now_add=True)  # Timestamp of prediction

    def __str__(self):
        return f"{self.user.username} - {self.prediction_result} - {self.prediction_date}"
