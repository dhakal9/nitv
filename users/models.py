from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import datetime
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField



# Extending User Model Using a One-To-One Link
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    dob = models.DateField(default=datetime.date.today)
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    EDUCATION_CHOICES = (
        ("AUT", "Austria"),
        ("DEU", "Germany"),
        ("NLD", "Neitherlands"),
    )
    
    P_CONTACT_CHOICES = (
        ('0', 'Email'),
        ('1', 'Phone'),
        ('2', 'None'),
    )
     
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=GENDER_CHOICES[0])
    education = models.CharField(max_length=100, choices=EDUCATION_CHOICES, default=EDUCATION_CHOICES[0])
    phone = PhoneNumberField(null=True)
    country = CountryField(blank=True)

    contact = models.CharField(max_length=1, choices=P_CONTACT_CHOICES, default=P_CONTACT_CHOICES[2])
    
    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
