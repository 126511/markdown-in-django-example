from django.db import models

import string
import random

# Create your models here.
class File(models.Model):
    id = models.CharField(max_length=16, primary_key=True, default=''.join(random.choices(string.ascii_letters+string.digits,k=16)))
    title = models.CharField(max_length=128)
    body = models.TextField()


    def __str__(self):
        return self.title


