from django.db import models

# Create your models here.


class HierarchyValue(models.Model):

    value = models.CharField(max_length=255)


class HierarchyName(models.Model):

    name = models.CharField(max_length=255)
    hierarchy_value = models.ForeignKey(HierarchyValue, on_delete=models.CASCADE,)


class SearchValues(models.Model):

    usage = models.IntegerField()
    part = models.IntegerField()


class PartUsageHierarchyName(models.Model):

    hierarchy_name = models.ForeignKey(HierarchyName, on_delete=models.CASCADE,)
    search_value = models.ForeignKey(SearchValues, on_delete=models.CASCADE,)
