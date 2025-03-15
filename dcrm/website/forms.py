from django import forms
from .models import Record

class AddRecordForm(forms.ModelForm):
    client_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Nazwa klienta",
        label_suffix=""
    )

    # Compute Section
    vcpu = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="vCPU",
        label_suffix="",
    )
    vram = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="RAM",
        label_suffix=""
    )
    adm_hours = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Godziny administracyjne",
        label_suffix="",
        initial="0"
    )
    vconnect = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="vConnect",
        label_suffix="",
        initial="0"
    )

    # Storage Section
    disk = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Dysk",
        label_suffix=""
    )
    disk_profile = forms.ChoiceField(
        choices=[("1", "1"), ("2", "2"), ("3", "3")],
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Profil wydajnościowy dysku",
        label_suffix="",
    )
    pbs = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="PBS",
        label_suffix=""
    )
    pbs_replication = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Backup replication",
        label_suffix="",
        initial="0"
    )

    # Networking Section
    ip = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="IP",
        label_suffix="",
        initial="0"
    )
    network = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Network",
        label_suffix="",
        initial="0"
    )
    dmz = forms.ChoiceField(
        choices=[("No", "No"), ("Yes", "Yes")],
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="DMZ",
        label_suffix=""
    )
    pub_net_speed = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Public Network Speed",
        label_suffix="",
        initial="100"
    )

    # Security Section
    fw_premium = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Firewall Premium",
        label_suffix="",
        initial="0"
    )
    geofw = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="GeoFirewall",
        label_suffix="",
        initial="0"
    )
    ipsec = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="IPSec",
        label_suffix="",
        initial="0"
    )
    ssl_vpn = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="SSL-VPN",
        label_suffix="",
        initial="0"
    )
    dns_guard = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="DNS Guard",
        label_suffix="",
        initial="0"
    )
    webfiltering = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Web Filtering",
        label_suffix="",
        initial="0"
    )
    ids_ips = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="IDS/IPS/AV",
        label_suffix="",
        initial="0"
    )
    vdom = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="VDOM",
        label_suffix="",
        initial="0"
    )

    # Licenses Section
    ws2022_1 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Windows Server 2022 (1Y)",
        label_suffix="",
        initial="0"
    )
    ws2022_3 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Windows Server 2022 (3Y)",
        label_suffix="",
        initial="0"
    )
    ws2022_cal_1 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Windows Server 2022 CAL (1Y)",
        label_suffix="",
        initial="0"
    )
    ws2022_cal_3 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Windows Server 2022 CAL (3Y)",
        label_suffix="",
        initial="0"
    )
    rds_cal_1 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="RDS CAL (1Y)",
        label_suffix="",
        initial="0"
    )
    rds_cal_3 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="RDS CAL (3Y)",
        label_suffix="",
        initial="0"
    )
    rds_cal_perpetual = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="RDS CAL (Perpetual)",
        label_suffix="",
        initial="0"
    )

    # General Information
    procedure = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Typ",
        label_suffix="",
        initial="Nowa maszyna"
    )
    is_accepted = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Accepted",
        label_suffix="",
        initial="No"
    )
    status = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Status",
        label_suffix="",
        initial="In progress"
    )

    class Meta:
        model = Record
        exclude = ("user", )