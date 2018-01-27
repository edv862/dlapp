from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Output(models.Model):
    TEXT = 'TEXT'
    LINE = 'LINE'
    PARAGRAPH = 'PARAGRAPH'

    SEARCH_TYPES = (
        (TEXT, 'Text Search'),
        (LINE, 'Line Search'),
        (PARAGRAPH, 'Paragraph Search'),
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

    file_name = models.CharField(
        max_length=255,
    )
    output_text = models.TextField(
        u'Texto extraido',
        blank=True,
        null=True
    )
    search_type = models.CharField(
        max_length=50,
        choices=SEARCH_TYPES,
        default=TEXT,
    )
    search_value = models.TextField()
