from django.db import models

class College(models.Model):
    college_name = models.CharField(max_length=200)
    college_logo = models.ImageField(upload_to='logos/')  # Saves uploaded logos in media/logos/
    college_profile = models.CharField(max_length=200)
    instructions = models.TextField()

    def __str__(self):
        return self.college_name