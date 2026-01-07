from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


ROLE=[
    (1, "manager"),
    (2, "user"),
]
STATUS =[
    (1, "new"),
    (2, "processing")
    ,(3, "done")
]

# Create your models here.
class UserStaff(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE, default=1)
    team = models.ForeignKey("Team",on_delete = models.CASCADE, null=True,blank=True,related_name="members")
    def __str__(self):
        return self.user.username


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    dateEnd = models.DateField()
    status = models.IntegerField(choices=STATUS, default=1)
    user = models.ForeignKey("UserStaff", on_delete=models.CASCADE,null=True,blank=True)
    team = models.ForeignKey("Team", on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    manager = models.ForeignKey("UserStaff", on_delete=models.CASCADE,null=True,blank=True,related_name="managed_team")
    def __str__(self):
        return self.name

