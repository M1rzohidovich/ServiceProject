from django.db import models
from main.models import InternalBlog, ExternalBlog


class IchkiMijoz(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=180)
    comment = models.TextField()
    cleaning_date = models.DateTimeField()
    upload_date = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(InternalBlog, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "IchkiMijoz"
        verbose_name_plural = "IchkiMijozs"


class TashqiMijoz(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=180)
    comment = models.TextField()
    cleaning_date = models.DateTimeField()
    upload_date = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(ExternalBlog, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "TashqiMijoz"
        verbose_name_plural = "TashqiMijozs"
