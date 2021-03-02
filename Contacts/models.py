from django.db import models

# Create your models h
class Contact(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name