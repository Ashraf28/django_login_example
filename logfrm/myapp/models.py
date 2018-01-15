from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProInf(models.Model):

    user = models.OneToOneField(User)

    portfol_site = models.URLField(blank=True)

    pro_pic = models.ImageField(upload_to='pro_pic', blank=True)

    def __str__ (self):
        return self.user.username
