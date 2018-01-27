from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Output(models.Model):
    SEARCH_TYPES = (
        (0, 'Text Search'),
        (1, 'Line Search'),
        (2, 'Paragraph Search'),
    )

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
    search_type = models.IntegerField(
        choices=SEARCH_TYPES,
        default=0,
    )
    search_value = models.TextField()
