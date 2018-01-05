from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Output(models.Model):
    # Usuario que creo el Output
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(
        auto_now_add=True,
        blank=True
    )
    output_text = models.TextField(
        u'Texto extraido',
        blank=True,
        null=True
    )
