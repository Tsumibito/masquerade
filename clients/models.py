from django.db import models
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    email = models.EmailField(blank=True, null=True, default=None, unique=True)
    phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    user = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)
    last_validated_session = models.ForeignKey(Session, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Visitor(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.client

    class Meta:
        verbose_name = 'Посетитель'
        verbose_name_plural = 'Посетители'

class VisitorVisit(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=True, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = 'Посешение'
        verbose_name_plural = 'Посещения'
