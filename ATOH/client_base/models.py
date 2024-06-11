from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class Person(models.Model):
    person_name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    patronym = models.CharField(max_length=64)

    class Meta:
        abstract = True
    
    def __str__(self):
        return ' '.join([self.person_name, self.surname, self.patronym])

    
class Status(models.Model):
    CLIENT_STATUS = [
        (0,'Not in work'),
        (1, 'In work'),
        (2, 'Rejected'),
        (3, 'Closed')
    ]
    status = models.CharField(max_length=20, choices=CLIENT_STATUS)
    
    def __str(self):
        return self.get_status_display()

class Responsible(Person, AbstractUser):
    class Meta:
        proxy = True

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Client(Person, models.Model):
    bank_number = models.IntegerField(unique=True)
    birth_date = models.DateField()
    INN = models.IntegerField(unique=True)
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, default=0)

    def __str__(self):
        return super().__str__()
    
    def save(self, *args, **kwargs):
        if self.pk is None and self.status_id is None:
            self.status = Status.objects.get(status='0')
        super().save(*args, **kwargs)
