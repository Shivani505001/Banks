from django.db import models

# Create your models here.
class bank(models.Model):
    ifsc = models.CharField(primary_key=True, max_length=255)
    bank_id = models.IntegerField(blank=True, null=True)
    branch = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    bank_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_branches'