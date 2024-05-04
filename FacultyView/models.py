from django.db import models
import uuid
from django.utils import timezone
import secrets
import datetime
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)

class UniqueID(models.Model):
    unique_id = models.CharField(max_length=32, default=get_random_string(length=32))


class Section(models.Model):
    section = models.CharField(max_length=2)

    def __str__(self) -> str:
        return self.section


class Year(models.Model):
    year = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(4)],
    )

    def __str__(self) -> str:
        return str(self.year)


class Branch(models.Model):
    branch = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.branch


class Student(models.Model):
    s_roll = models.CharField(max_length=20, primary_key=True)
    s_fname = models.CharField(max_length=20)
    s_lname = models.CharField(max_length=20)
    s_branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    s_section = models.ForeignKey(Section, on_delete=models.CASCADE)
    s_year = models.ForeignKey(Year, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.s_fname} {self.s_lname} - {self.s_roll} - {self.s_branch}({self.s_year}{self.s_section})"
