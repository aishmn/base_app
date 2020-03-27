from django.db import models
from django.urls import reverse
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.utils import timezone
# Create your models here.


class Portfollio(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    contact = models.CharField(max_length=254)
    birthdate = models.DateField(default=None)
    image = models.ImageField(default='default.jpg',
                              upload_to="portfollio_images")
    image2 = models.ImageField(default='default.jpg',
                               upload_to="portfollio_images")
    current_city = models.CharField(max_length=250)
    current_country = models.CharField(max_length=250)
    current_location = models.CharField(max_length=250)
    job_title = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name


class Education(models.Model):
    degree = models.CharField(max_length=250)
    start_date = models.CharField(max_length=250)
    end_date = models.CharField(max_length=250)
    university = models.CharField(max_length=250)
    desc = models.TextField()

    def __str__(self):
        return self.degree


class Service(models.Model):
    title = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)
    desc = models.TextField()

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=250)
    percentage = models.IntegerField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.IntegerField()
    address = models.CharField(max_length=250)
    website = models.URLField(max_length=200, default="www.google.com")

    def __str__(self):
        return self.title


class ContactMeMessage(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=250)
    desc = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(default='default.jpg',
                              upload_to="portfollio_images")
    text = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"slug": self.slug})


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Blog)
