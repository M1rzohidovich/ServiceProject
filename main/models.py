from os.path import splitext

from django.db import models
from django.utils.text import slugify


def slugify_upload(instance, filename):
    folder = instance._meta.model.__name__
    name, ext = splitext(filename)
    try:

        name_t = slugify(name)
        if name_t is None:
            name_t = name
        path = folder + "/" + name_t + ext
    except:
        path = folder + "/default" + ext

    return path


class InternalBlog(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to=slugify_upload)
    img2 = models.ImageField(upload_to=slugify_upload, blank=True)
    img3 = models.ImageField(upload_to=slugify_upload, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class ExternalBlog(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to=slugify_upload)
    img2 = models.ImageField(upload_to=slugify_upload, blank=True)
    img3 = models.ImageField(upload_to=slugify_upload, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Announcement(models.Model):
    title = models.CharField(max_length=50)
    img1 = models.ImageField(upload_to=slugify_upload)
    img2 = models.ImageField(upload_to=slugify_upload, blank=True)
    img3 = models.ImageField(upload_to=slugify_upload, blank=True)
    description = models.TextField()

    class Meta:
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"

    def __str__(self):
        return self.title


class WorkerContact(models.Model):
    Fullname = models.CharField(max_length=120)
    img = models.ImageField(upload_to=slugify_upload)
    the_task = models.CharField(max_length=100)
    Rating = models.CharField(max_length=60)

    class Meta:
        verbose_name = "WorkerContact"
        verbose_name_plural = "WorkerContacts"

    def __str__(self):
        return self.Fullname
