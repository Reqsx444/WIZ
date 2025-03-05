from django.db import models


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    client_name = models.CharField(max_length=50)
    vcpu = models.CharField(max_length=50)
    vram = models.CharField(max_length=50)
    disk = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    pbs = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    dmz = models.CharField(max_length=50)

    def __str__(self):
        return(f"{self.client_name}")