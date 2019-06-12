from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title


class InfoRsp(models.Model):
    temperature = models.TextField()
    seaLevel = models.TextField()
    time = models.TextField()
    date = models.TextField()
    serialTag = models.TextField()
    position = models.TextField()

    def __str__(self):
        return "time: "+self.time + " date: "+self.date
