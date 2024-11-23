from django.db import models

# Create your models here.

class Profile(models.Model):
    image = models.ImageField(upload_to='profile/')
    full_name = models.CharField(max_length=150)
    subject = models.CharField(max_length=100)
    bio = models.TextField()


    def __str__(self):
        return self.full_name


class Social(models.Model):
    logo = models.ImageField(upload_to='social/')
    name = models.CharField(max_length=100)
    url = models.URLField()
    imagine = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Info(models.Model):
    email = models.EmailField()
    number = models.CharField(max_length=15)
    location = models.CharField(max_length=150)
    location_url = models.URLField()

    def __str__(self):
        return f"{self.id}"


class Language(models.Model):
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=20, choices=(('Beginner', 'Beginner'), ('Elementary', 'Elementary'),\
                                                     ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Native', 'Native')))
    image = models.ImageField(upload_to='language/')


    def __str__(self):
        return self.name


class LatestProject(models.Model):
    image = models.ImageField(upload_to='project/')
    title = models.CharField(max_length=100)
    body = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title


class Experience(models.Model):
    logo = models.ImageField(upload_to='experience/')
    job = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    location_url = models.URLField()
    start_date = models.DateField()
    end_date = models.DateField()


    def __str__(self):
        return self.job

class Skill(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=(('KS', 'Key skills'), ('AS', 'Additional skills')))

    def __str__(self):
        return self.name


class Education(models.Model):
    logo = models.ImageField(upload_to='education/')
    academy = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()


    def __str__(self):
        return self.academy