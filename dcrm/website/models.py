from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    client_name = models.CharField(max_length=50)
    vcpu = models.IntegerField(
        null=True, blank=True,
        validators=[MinValueValidator(1, "Minimalna wartość to 1"), MaxValueValidator(32, "Maksymalna wartość to 32")]
    )
    vram = models.IntegerField(
        null=True, blank=True,
        validators=[MinValueValidator(1, "Minimalna wartość to 1"), MaxValueValidator(32, "Maksymalna wartość to 32")]
    )
    disk = models.IntegerField(
        null=True, blank=True,
        validators=[MinValueValidator(20, "Minimalna wartość to 20"), MaxValueValidator(1000, "Maksymalna wartość to 1000")]
    )
    ip = models.IntegerField(
        null=True, blank=True, default='0',
        validators=[MinValueValidator(0, "Minimalna wartość to 0"), MaxValueValidator(20, "Maksymalna wartość to 20")]
    )
    pbs = models.IntegerField(null=True, blank=True)
    network = models.CharField(max_length=50)
    pub_net_speed = models.IntegerField(
        null=True, blank=True, default='100',
        validators=[MinValueValidator(100, "Minimalna wartość to 100"), MaxValueValidator(1000, "Maksymalna wartość to 1000")]
    )
    dmz = models.CharField(max_length=50)
    disk_profile = models.IntegerField(
        null=True, blank=True, default='1',
        validators=[MinValueValidator(1, "Minimalna wartość to 1"), MaxValueValidator(3, "Maksymalna wartość to 3")]
    )
    pbs_replication = models.IntegerField(null=True, blank=True)
    vconnect = models.CharField(max_length=50, null=True, blank=True)
    adm_hours = models.IntegerField(null=True, blank=True)
    ws2022_1 = models.IntegerField(null=True, blank=True)
    ws2022_3 = models.IntegerField(null=True, blank=True)
    ws2022_cal_1 = models.IntegerField(null=True, blank=True)
    ws2022_cal_3 = models.IntegerField(null=True, blank=True)
    rds_cal_1 = models.IntegerField(null=True, blank=True)
    rds_cal_3 = models.IntegerField(null=True, blank=True)
    rds_cal_perpetual = models.IntegerField(null=True, blank=True)
    fw_premium = models.CharField(max_length=50, null=True, blank=True)
    geofw = models.CharField(max_length=50, null=True, blank=True)
    ipsec = models.CharField(max_length=50, null=True, blank=True)
    ssl_vpn = models.CharField(max_length=50, null=True, blank=True)
    dns_guard = models.CharField(max_length=50, null=True, blank=True)
    webfiltering = models.CharField(max_length=50, null=True, blank=True)
    ids_ips = models.IntegerField(null=True, blank=True)
    vdom = models.CharField(max_length=50, null=True, blank=True)
    procedure = models.CharField(max_length=50, null=True, blank=True, default='Nowa maszyna')
    is_accepted = models.CharField(max_length=50, null=True, blank=True, default='No')
    status = models.CharField(max_length=50, null=True, blank=True, default='In progress')

    def clean(self):
        """Walidacja: pbs musi być równe disk oraz pbs_replication musi być równe pbs lub 0"""
        errors = {}

        if self.pbs is not None and self.disk is not None and self.pbs != self.disk:
            errors["pbs"] = "Wartość PBS musi być równa wartości Disk."

        if self.pbs_replication is not None and self.pbs is not None:
            if self.pbs_replication != self.pbs and self.pbs_replication != 0:
                errors["pbs_replication"] = "Wartość PBS Replication musi być równa wartości PBS lub 0."

        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return self.client_name