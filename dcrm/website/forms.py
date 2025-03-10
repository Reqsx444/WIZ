from django import forms
from .models import Record

class AddRecordForm(forms.ModelForm):
    client_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Client Name", "class":"form-control"}), label="")
    vcpu = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"vCPU", "class":"form-control"}), label="")
    vram = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"RAM", "class":"form-control"}), label="")
    disk = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Disk", "class":"form-control"}), label="")
    ip = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"IP", "class":"form-control"}), label="")
    pbs = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"PBS", "class":"form-control"}), label="")
    network = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Network", "class":"form-control"}), label="")
    dmz = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"DMZ", "class":"form-control"}), label="")
    disk_profile = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Disk profile", "class":"form-control"}), label="")
    pbs_replication = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Backup replication", "class":"form-control"}), label="")
    vconnect = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"vConnect", "class":"form-control"}), label="")
    adm_hours = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Adm hours", "class":"form-control"}), label="")
    ws2022_1 = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"ws2022_1", "class":"form-control"}), label="")
    ws2022_3 = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"ws2022_3", "class":"form-control"}), label="")
    ws2022_cal_1 = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"ws2022_cal_1", "class":"form-control"}), label="")
    ws2022_cal_3 = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"ws2022_cal_3", "class":"form-control"}), label="")
    rds_cal_1 = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"rds_cal_1", "class":"form-control"}), label="")
    rds_cal_3 = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"rds_cal_3", "class":"form-control"}), label="")
    rds_cal_perpetual = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"rds_cal_perpetual", "class":"form-control"}), label="")
    fw_premium = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"fw_premium", "class":"form-control"}), label="")
    geofw = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"geofw", "class":"form-control"}), label="")
    ipsec = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"ipsec", "class":"form-control"}), label="")
    ssl_vpn = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"ssl_vpn", "class":"form-control"}), label="")
    dns_guard = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"dns_guard", "class":"form-control"}), label="")
    webfiltering = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"webfiltering", "class":"form-control"}), label="")
    ids_ips = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"ids_ips", "class":"form-control"}), label="")
    vdom = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"vdom", "class":"form-control"}), label="")
    is_accepted = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"is_accepted", "class":"form-control"}), label="")
    status = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"status", "class":"form-control"}), label="")

    class Meta:
        model = Record
        exclude = ("user", )