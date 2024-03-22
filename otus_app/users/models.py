from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import ModelForm

# Create your models here.


class Users_info(models.Model):
        ID = models.IntegerField('ID',primary_key=True)
        UserName = models.CharField('UserName',max_length=255)
        FirstName = models.CharField('FirstName', max_length=255)
        LastName = models.CharField('LastName', max_length=255)
        Email = models.CharField('Email', max_length=255)
        Phone = PhoneNumberField('Phone',unique=True, null=False, blank=False)

        #objects = models.Manager()

        class Meta:
            verbose_name_plural = "Пользователи"


        def __str__(self):
             #return f'{[self.ID,self.UserName, self.FirstName, self.LastName, self.Email]!r}'
             return self.FirstName
                    # self.FirstName,
                    # self.LastName,
                    # self.Email,
                    # self.Phone)