from django.db import models

from django.utils.translation import gettext_lazy as _


# Create your models here.

class Privacy_and_Policy(models.Model):
    heading = models.CharField(_('Heading'), max_length=100)
    Description = models.TextField(_('Description'))

    def __str__(self):
        return self.heading


class Contact_Us(models.Model):
    first_name = models.CharField(_('FirstName'), max_length=254)
    last_name = models.CharField(_('LastName'), max_length=254)
    nickname = models.CharField(max_length=50)
    email = models.EmailField(_('Email Address'))
    mobile = models.CharField(_('Mobile Number'), max_length=15)
    subject = models.CharField(_('Subject'), max_length=254)
    message = models.TextField(_('Message'))
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        contact = str(self.nickname)
        return contact


class Terms_of_Use(models.Model):
    heading = models.CharField(_('Heading'), max_length=100)
    Description = models.TextField(_('Description'))

    def __str__(self):
        return self.heading



class Shopping_Help(models.Model):
    questions_heading = models.CharField(_('Heading'), max_length=100)
    Answer = models.TextField(_('Answer'))

    def __str__(self):
        return self.questions_heading
