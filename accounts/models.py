from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        db_table = "Profile"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"