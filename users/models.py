# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

  """ Custom User Model """

  # GENDER_CHOICES
  GENDER_MALE   = "male"
  GENDER_FEMALE = "female"
  GENDER_OTHER  = "other"

  GENDER_CHOICES = (
    (GENDER_MALE, "Male"),
    (GENDER_FEMALE, "Female"),
    (GENDER_OTHER, "Other")
  )

  # LANGUANGE_CHOICES
  LANGUANGE_ENGLISH = "en"
  LANGUANGE_KOREAN  = "kr"
  LANGUANGE_INDONESIAN = "ind"

  LANGUANGE_CHOICES = (
    (LANGUANGE_ENGLISH, "English"),
    (LANGUANGE_KOREAN, "Korean"),
    (LANGUANGE_INDONESIAN, "Indonesian")
  )

  # CURRENCY_CHOICES
  CURRENCY_US = "usd"
  CURRENCY_KOREA = 'krw'
  CURRENCY_INDONESIA = 'rp'

  CURRENCY_CHOICES = (
    (CURRENCY_US, "USD"),
    (CURRENCY_KOREA, "KRW"),
    (CURRENCY_INDONESIA, "RP")
  )

  avatar = models.ImageField(blank=True)
  gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
  bio = models.TextField(blank=True)
  birthdate = models.DateField(blank=True, null=True)
  language = models.CharField(choices=LANGUANGE_CHOICES, max_length=25, blank=True)
  currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
  superhost = models.BooleanField(default=False)
