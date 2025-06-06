# models.py
from django.db import models

class Reminder(models.Model):
    NOTIFICATION_METHODS = [
        ('SMS', 'SMS'),
        ('EMAIL', 'Email'),
    ]
    
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    notification_method = models.CharField(
        max_length=5,
        choices=NOTIFICATION_METHODS,
        default='EMAIL'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['date', 'time']
    
    def __str__(self):
        return f"Reminder for {self.date} at {self.time} via {self.get_notification_method_display()}"