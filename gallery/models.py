from django.db import models


class Photography(models.Model):

    CATEGORY_CHOICES = (
        ("NEBULA", "Nebula"),
        ("START", "Star"),
        ("GALAXY", "Galaxy"),
        ("PLANET", "Planet"),
    )

    name = models.CharField(max_length=100, null=False, blank=False)
    credits = models.CharField(max_length=200, null=False, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='')
    description = models.TextField(null=False, blank=False)
    photo = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return f"Photography [name={self.name}]"
