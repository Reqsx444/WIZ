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
        initial=0
    )

    # Storage Section
    disk = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Dysk",
        label_suffix=""
    )
    disk_profile = forms.ChoiceField(
        choices=[(1, "1"), (2, "2"), (3, "3")],
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
        label="PBS - replikacja",
        label_suffix="",
        initial="0"
    )

    # Networking Section
    ip = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Dodatkowe publiczne IP",
        label_suffix="",
        initial="0"
    )
    network = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")],
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Sieć wewnętrzna 1Gbit/s",
        label_suffix=""
    )
    dmz = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")],
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="DMZ",
        label_suffix=""
    )
    pub_net_speed = forms.ChoiceField(
        choices=[(100, "100Mbps"), (200, "200Mbps"), (300, "300Mbps"), (400, "400Mbps"), (500, "500Mbps"), (600, "600Mbps"), (700, "700Mbps"), (800, "800Mbps"), (900, "900Mbps"), (1000, "1000Mbps")],
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Przepustowość sieci publicznej:",
        label_suffix=""
    )

    # Security Section
    fw_premium = forms.ChoiceField(
        choices=[(0, "0"), (1, "10"), (2, "20"), (3, "30")],
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="DSS Firewall Premium",
        label_suffix=""
    )
    geofw = forms.ChoiceField(
        choices=[(0, 1), ("Yes", "Yes")],
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="DSS GeoFirewall",
        label_suffix=""
    )
    ipsec = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")],
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="DSS IPSec",
        label_suffix=""
    )
    ssl_vpn = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="DSS konto SSL-VPN",
        label_suffix="",
        initial="0"
    )
    dns_guard = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")],
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="DSS Guard DNS",
        label_suffix=""
    )
    webfiltering = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")],
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="DSS Webfiltering",
        label_suffix=""
    )
    ids_ips = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")],
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="DSS IDS/IPS/AV 100Mbit/s",
        label_suffix="",
        initial="0"
    )
    vdom = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")],
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="DSS vDOM",
        label_suffix=""
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
    procedure = forms.ChoiceField(
        choices=[("Nowy VPS", "Nowy VPS"), ("Rozbudowa obecnego VPS", "Rozbudowa obecnego VPS")],
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Typ",
        label_suffix="",
    )
    is_accepted = forms.ChoiceField(
        choices=[(0, "Nie"), (1, "Tak")],
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Zaakceptowane",
        label_suffix="",
    )
    status = forms.ChoiceField(
        choices=[("W trakcie", "W trakcie"), ("Zakończone", "Zakończone")],
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Status",
        label_suffix="",
    )

    class Meta:
        model = Record
        exclude = ("user", )