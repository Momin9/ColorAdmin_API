from django.db import models

from django.utils.translation import gettext_lazy as _


# Create your models here.

class Privacy_and_Policy(models.Model):
    heading = models.CharField(_('Category name'), max_length=100)
    Description = models.TextField(_('Description'))

    def __str__(self):
        return self.heading


class Contact_Us(models.Model):
    first_name = models.CharField(_('Unique FirstName'), max_length=254)
    last_name = models.CharField(_('Unique LastName'), max_length=254)
    nickname = models.CharField(max_length=50)
    email = models.EmailField(_('Email Address'))
    mobile = models.CharField(_('Mobile Number'), max_length=15)
    subject = models.CharField(_('Reason'), max_length=254)
    message = models.TextField(_('Message'))
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        contact = {"name": self.name, "number": self.mobile}
        return contact


