from __future__ import unicode_literals

import datetime

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from PIL import Image
from notifications.signals import notify
from rest_framework.authtoken.models import Token

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    is_donor = models.BooleanField(default=False)

    objects = UserManager()

#
# @receiver(post_save, sender=User)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)



class Account(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    email_confirmed = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=15, null=True)
    street= models.CharField(max_length=50, null=True)
    road = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    post_code = models.CharField(max_length=50, null=True)

@receiver(post_save, sender=User)
def update_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)
        instance.account.save()

    def __str__(self):
        return self.user.email




class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bloodGroup = models.CharField(max_length=2, null=True)
    birth_date = models.DateField(null=True)
    last_donated_date = models.DateField(null=True)
    capable = models.BooleanField(default=True)



@receiver(post_save, sender=User)
def update_user_donor(sender, instance, created, **kwargs):
    if created and instance.is_donor:
        Donor.objects.create(user=instance)
        instance.donor.save()

    def __str__(self):
        return self.user.email





class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bloodGroup = models.CharField(max_length=5, null=False, blank=False)
    street= models.CharField(max_length=50, null=True)
    road = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    post_code = models.CharField(max_length=50, null=True)
    time = models.DateField(null=False, blank=False)
    bags = models.IntegerField(null=False, blank=False)



@receiver(post_save, sender=Request)
def update_request_notification(sender, instance, created, **kwargs):
    if created:
        bloodGroup = instance.bloodGroup
        city = instance.city
        possible_donor_ids = list(Donor.objects.filter(bloodGroup=bloodGroup).values_list("id", flat=True))
        possible__account_ids = list(Account.objects.filter(city__iexact=city).values_list("id", flat=True))
        userlist = list(User.objects.filter(account__id__in=possible__account_ids, donor__id__in=possible_donor_ids).exclude(id = instance.user.id))
        if userlist:
           for receiver in userlist:
                Notification.objects.create(user=receiver, request=instance)

    def __str__(self):
        return self.bloodGroup




class Blood(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    o_pos = models.IntegerField(default=0)
    o_neg = models.IntegerField(default=0)
    a_pos = models.IntegerField(default=0)
    a_neg = models.IntegerField(default=0)
    b_pos = models.IntegerField(default=0)
    b_neg = models.IntegerField(default=0)
    ab_pos = models.IntegerField(default=0)
    ab_neg = models.IntegerField(default=0)


@receiver(post_save, sender=User)
def update_user_blood(sender, instance, created, **kwargs):
    if created and instance.is_donor is False:
        Blood.objects.create(user=instance)
        instance.blood.save()

    def __str__(self):
        return self.user.email

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    finished = models.BooleanField(default=False)
    interested = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
