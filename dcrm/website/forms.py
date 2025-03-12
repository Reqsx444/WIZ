from django import forms
from .models import Record

class AddRecordForm(forms.ModelForm):
    client_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Client Name",
        label_suffix=""
    )

    # Compute Section
    vcpu = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="vCPU",
        label_suffix=""
    )
    vram = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="RAM",
        label_suffix=""
    )
    adm_hours = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Adm hours",
        label_suffix=""
    )
    vconnect = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="vConnect",
        label_suffix=""
    )

    # Storage Section
    disk = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Disk",
        label_suffix=""
    )
    disk_profile = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Disk profile",
        label_suffix=""
    )
    pbs = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="PBS",
        label_suffix=""
    )
    pbs_replication = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Backup replication",
        label_suffix=""
    )

    # Networking Section
    ip = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="IP",
        label_suffix=""
    )
    network = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Network",
        label_suffix=""
    )
    dmz = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="DMZ",
        label_suffix=""
    )
    pub_net_speed = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Public Network Speed",
        label_suffix=""
    )

    # Security Section
    fw_premium = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Firewall Premium",
        label_suffix=""
    )
    geofw = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="GeoFirewall",
        label_suffix=""
    )
    ipsec = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="IPSec",
        label_suffix=""
    )
    ssl_vpn = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="SSL-VPN",
        label_suffix=""
    )
    dns_guard = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="DNS Guard",
        label_suffix=""
    )
    webfiltering = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Web Filtering",
        label_suffix=""
    )
    ids_ips = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="IDS/IPS/AV",
        label_suffix=""
    )
    vdom = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="VDOM",
        label_suffix=""
    )

    # Licenses Section
    ws2022_1 = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Windows Server 2022 (1Y)",
        label_suffix=""
    )
    ws2022_3 = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Windows Server 2022 (3Y)",
        label_suffix=""
    )
    ws2022_cal_1 = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Windows Server 2022 CAL (1Y)",
        label_suffix=""
    )
    ws2022_cal_3 = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Windows Server 2022 CAL (3Y)",
        label_suffix=""
    )
    rds_cal_1 = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="RDS CAL (1Y)",
        label_suffix=""
    )
    rds_cal_3 = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="RDS CAL (3Y)",
        label_suffix=""
    )
    rds_cal_perpetual = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="RDS CAL (Perpetual)",
        label_suffix=""
    )

    # General Information
    is_accepted = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Accepted",
        label_suffix=""
    )
    status = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Status",
        label_suffix=""
    )

    class Meta:
        model = Record
        exclude = ("user", )