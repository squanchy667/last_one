from django.db import models


class CONtacts(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name


class Employer(models.Model):
    name = models.CharField(max_length=50)
    identifier = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()
    contacts = models.ManyToManyField(CONtacts)

    def __str__(self):
        return self.name



