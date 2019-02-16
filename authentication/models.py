from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone
from django.core.validators import RegexValidator
from django import forms

class MyUserManager(BaseUserManager):
    def create_user(self, user_name, first_name, middel_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not user_name:
            raise ValueError('Users must have an usrer name address')

        user = self.model(
            user_name=user_name,
            first_name=first_name,
            middel_name=middel_name,  
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, first_name, middel_name,  password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            user_name,
            first_name,
            middel_name,
            password=password,
        )
        # user.date_of_birth = timezone.now() - datetime.timedelta(days=30)
        user.is_admin = True
        user.save(using=self._db)
        return user

class Role(models.Model):
    role_name      = models.CharField(max_length=10)
    
    def __str__(self):
        return self.role_name

class User(AbstractBaseUser):
    SEX_CHOICES         = (('m', 'Male',), ('f', 'Female',))
    MARITAL_CHOICES     = (('m', 'Marriage',), ('N', 'Not Marriage',), ('d', 'Divorce',))
    disablity_choices   = (('d', 'No Disable'), ('e', 'Eay Disable'),)
    RELIGION_CHOICES    = (('i', 'Islam'), ('c', 'Christianity'), ('b', 'Buddhism'),('h', 'Hinduism'),('o', 'Other'))
    EDUCATION_CHOICES   = (
                            ('d', 'Doctoral degree'), 
                            ('m', "Master's degree"), 
                            ('b', "Bachelor's degree"),
                            ('dp', 'Diploma'),
                            ('p', 'Preparatory'),
                            ('s', 'Secondary'),
                            ('e', 'Elementary'),
                            ('l', 'Li')
                            )
    BLOOD_CHOICES       = (
                            ('o+', 'O-positive'), 
                            ('o-', 'O-negative'), 
                            ('a+', 'A-positive'),
                            ('a-', 'A-negative'),
                            ('b+', 'B-positive'),
                            ('b-', 'B-negative'),
                            ('ab+', 'AB-positive'),
                            ('ab-', 'AB-negative')
                            )

    valid_phone  = RegexValidator(regex=r'^\+?1?\d{10,15}$', message="Phone number must be entered in the format : 09******** or +2519********")

    first_name               = models.CharField(max_length=255, verbose_name='Your Name')
    middel_name              = models.CharField(max_length=255, verbose_name='Father Name')
    last_name                = models.CharField(max_length=255, verbose_name='Grand Father Name')
    mother_name              = models.CharField(max_length=255, verbose_name='Mother Name')
    date_of_birth            = models.DateField(default=timezone.now(), verbose_name='Date Of Birth')
    place_of_birth           = models.CharField(max_length=100, verbose_name='Place Of Birth')
    sex                      = models.CharField(max_length=2, choices=SEX_CHOICES)
    imgage                   = models.ImageField(max_length=255, default='admin-avatar.png', upload_to='profile', verbose_name='Profile Photo')
    blood_type               = models.CharField(max_length=2, choices=BLOOD_CHOICES)
    educationl_level         = models.CharField(max_length=2, choices=EDUCATION_CHOICES)
    licence_number           = models.CharField(max_length=20, verbose_name='Licence Number')
    nationality              = models.CharField(max_length=255, verbose_name='Nationality')
    region                   = models.CharField(max_length=255, verbose_name='Reigin')
    zone                     = models.CharField(max_length=255, verbose_name='Zone')
    wereda                   = models.CharField(max_length=255, verbose_name='Wereda')
    kebele                   = models.CharField(max_length=255, verbose_name='Kebeke')
    home_number              = models.CharField(max_length=20, verbose_name='Home Number')
    phone_number             = models.CharField(max_length=20, validators=[valid_phone], verbose_name='Phone Number')
    emergency_contact        = models.CharField(max_length=20, validators=[valid_phone], verbose_name='Emergency Contact')
    medical_status           = models.CharField(max_length=255, verbose_name='Medical Status')
    career                   = models.CharField(max_length=255, verbose_name='Job Title')      
    marital_status           = models.CharField(max_length=2, choices=MARITAL_CHOICES)
    religion                 = models.CharField(max_length=2, choices=RELIGION_CHOICES)
    disablity                = models.CharField(max_length=2, choices=disablity_choices, default='d', verbose_name='Disablity')
    issue_date               = models.DateField(default=timezone.now(), verbose_name='Issu Date')
    user_name                = models.CharField(max_length=255, verbose_name='User Name', unique=True)
    email                    = models.EmailField(max_length=255, verbose_name='Email Address', blank=True, null=True)
    role                     = models.ManyToManyField(Role)
    is_admin                 = models.BooleanField(default=False)
    is_active                = models.BooleanField(default=True)

        
    objects = MyUserManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['first_name', 'middel_name']

    class Meta:
        verbose_name_plural = 'All User Profile'

    def __str__(self):
        return self.user_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def full_name(self):
        return '{} {} {}'.format(self.first_name, self.middel_name, self.last_name)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    
class Region(models.Model):
    region_name   = models.CharField(max_length=255, verbose_name='Region Name', unique=True)
    region_admin  = models.OneToOneField(User, on_delete=models.CASCADE, related_name="region_name",
     limit_choices_to={'role__role_name': 'rg_admin'})

    class Meta:
        verbose_name_plural = '1 Region'

    def __str__(self):
        return self.region_name

    
class Zone(models.Model):
    zone_name   = models.CharField(max_length=255, verbose_name='Zone Name', unique=True)
    region      = models.OneToOneField(Region, on_delete=models.CASCADE, related_name="region")
    zone_admin  = models.OneToOneField(User, on_delete=models.CASCADE, related_name="zone_admin",
     limit_choices_to={'role__role_name': 'zn_admin'})

    class Meta:
        verbose_name_plural = '2 Zone'

    def __str__(self):
        return self.zone_name
   
class Wereda(models.Model):
    wereda_name   = models.CharField(max_length=255, verbose_name='Wereda Name', unique=True)
    zone          = models.OneToOneField(Zone, on_delete=models.CASCADE, related_name="zone")
    wereda_admin  = models.OneToOneField(User, on_delete=models.CASCADE, related_name="wereda_name",
    limit_choices_to={'role__role_name': 'wr_admin'})
   
    class Meta:
        verbose_name_plural = '3 Wereda'

    def __str__(self):
        return self.wereda_name

class Kebele(models.Model):
    kebele_name   = models.CharField(max_length=255, verbose_name='Kebele Name', unique=True)
    wereda        = models.OneToOneField(Wereda, on_delete=models.CASCADE, related_name="werede")
    kebele_admin  = models.OneToOneField(User, on_delete=models.CASCADE, related_name="kebele_name",
    limit_choices_to={'role__role_name': 'kb_admin'})

    class Meta:
        verbose_name_plural = '4 Kebele'

    def __str__(self):
        return self.kebele_name
  
class Orgenizaion(models.Model):
    orgenization_name   = models.CharField(max_length=255, verbose_name='Kebele Name', unique=True)
    orgenization_admin  = models.OneToOneField(User, on_delete=models.CASCADE, related_name="orgenization_name",
    limit_choices_to={'role__role_name': 'org_admin'})

    class Meta:
        verbose_name_plural = '5 Orgenizaion'

    def __str__(self):
        return self.orgenization_name
  