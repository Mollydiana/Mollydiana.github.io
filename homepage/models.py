from django.db import models


class Home(models.Model):
    image = models.ImageField(upload_to='_old_static/img')

    def __unicode__(self):
        return self.name


class AboutMe(models.Model):
    image = models.ImageField(upload_to='_old_static/img')

    def __unicode__(self):
        return self.name