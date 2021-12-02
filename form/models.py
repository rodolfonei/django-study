from django.db import models

class Request(models.Model):
    description = models.TextField(max_length=30)
    email = models.EmailField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()
    send_mail = models.BooleanField(default=True)

    MOTIVATION_CHOICES = (
        ('Vacation', 'Vacation'),
        ('Holiday', 'Holiday'),
        ('Sick', 'Sick')
    )

    motivation = models.CharField(max_length=60, choices=MOTIVATION_CHOICES)
    


