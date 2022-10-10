# from django.db import models
# from django.contrib.auth.models import User


# # # Create your models here.
# class Employee(models.Model):
#     name= models.CharField(max_length=100)
#     mail_id=models.CharField(max_length=100)
#     contact= models.CharField(max_length=100)
#     dept= models.CharField(max_length=100)
#     join_date=models.DateField(null=True,blank=True)
#     passwd=models.CharField(max_length=200)
#     class Meta:
#         ordering = ('name', )

#     def __str__(self):
#         return f'{self.name}'
# #     # def get_absolute_url(self):
# #     #     return reverse('book-detail', args=[str(self.id)])
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class EmployeeManager(BaseUserManager):
    def create_user(self,name,email, join_date, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """

        user = self.model(
            email=email,
            join_date =join_date,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class Employee(AbstractBaseUser):
    name=models.CharField(max_length=100)
    email = models.CharField(max_length=255,)
    join_date = models.DateField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    objects = EmployeeManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

