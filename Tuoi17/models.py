from django.db import models

class Registration(models.Model):
    ho_ten = models.CharField(max_length=100)
    ngay_sinh = models.DateField()

    def __str__(self):
        return self.ho_ten
