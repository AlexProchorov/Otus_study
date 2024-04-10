from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import ModelForm



class Users_info(models.Model):
        ID = models.AutoField('ID',primary_key=True)
        UserName = models.CharField('UserName',max_length=255)
        FirstName = models.CharField('FirstName', max_length=255, blank=True)
        LastName = models.CharField('LastName', max_length=255, blank=True)
        Email = models.EmailField('Email', max_length=255, blank=True)
        Phone = PhoneNumberField('Phone', null=True, blank=True)



        class Meta:
            verbose_name_plural = "Пользователи"


        def __str__(self) -> str:
             return self.FirstName


