from django.db import models


class Fakulte(models.Model):
    name = models.CharField(max_length = 200)


class Bolum(models.Model):
    fakulte = models.ForeignKey(Fakulte)
    name = models.CharField(max_length = 200)


class Ogrenci(models.Model):
    bolum = models.ForeignKey(Bolum)
    name = models.CharField(max_length = 200)
    surname = models.CharField(max_length = 200)
