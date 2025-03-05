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

    class Meta:
        model = Record
        exclude = ("user", )