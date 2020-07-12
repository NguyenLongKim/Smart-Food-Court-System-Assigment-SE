from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth='2000-01-01', user_type=1, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            user_type=user_type,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth='2000-01-01', user_type=4, password=None):
        user = self.create_user(
            email=email,
            password=password,
            date_of_birth=date_of_birth,
            user_type=4,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Customer'),
        (2, 'VendorOwner'),
        (3, 'Cook'),
        (4, 'Manager'),
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_admin = models.BooleanField(default=False)

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'user_type']
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class VendorOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'VendorOwner'
        verbose_name_plural = 'VendorOwners'


class Cook(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    work_for = models.ForeignKey(VendorOwner, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cook'
        verbose_name_plural = 'Cooks'


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_staff = True

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'
