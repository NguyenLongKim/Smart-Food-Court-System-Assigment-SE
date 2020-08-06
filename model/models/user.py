from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


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

        if user_type == 1:
            Customer.objects.set_user(user=user, user_type=user_type)
        elif user_type == 2:
            Cook.objects.set_user(user=user, user_type=user_type)
        elif user_type == 3:
            VendorOwner.objects.set_user(user=user, user_type=user_type)
        elif user_type == 4:
            Manager.objects.set_user(user=user, user_type=user_type)
        return user

    def create_superuser(self, email, date_of_birth='2000-01-01', user_type=4, password=None):
        user = self.create_user(
            email=email,
            password=password,
            date_of_birth=date_of_birth,
            user_type=4,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserTypeManager(models.Manager):
    def set_user(self, user, user_type):
        userType = self.create(user=user)
        userType.save(using=self._db)
        return userType


class User(AbstractBaseUser):
    USER_TYPE_CHOICES = (
        (1, 'Customer'),
        (2, 'Cook'),
        (3, 'VendorOwner'),
        (4, 'Manager'),
    )
    first_name = models.CharField(
        verbose_name='first name',
        max_length=30,
        default='None',
    )
    last_name = models.CharField(
        verbose_name='last name',
        max_length=50,
        default='None',
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
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

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)
    objects = UserTypeManager()

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class VendorOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    objects = UserTypeManager()

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'VendorOwner'
        verbose_name_plural = 'VendorOwners'


class Cook(models.Model):
    from .vendor import Vendor
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    work_for = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    objects = UserTypeManager()

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Cook'
        verbose_name_plural = 'Cooks'


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_staff = True
    objects = UserTypeManager()

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'
