import openpyxl
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddRecordForm
from .models import Record
from django.http import HttpResponse

def home(request):

    records = Record.objects.all()

    #Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged In ...")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_id = Record.objects.get(id=pk)
        delete_id.delete()
        messages.success(request, "Record Deletes Successfully...")
        return redirect('home')
    else:
        messages.success(request, "You Must be logged in to do that...")
        return render(request, 'home.html')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in...")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated...")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You Must be logged in to do that...")
        return render(request, 'home.html')   

#Testy generowania wyceny

def generate_xlsx(request, record_id):
    # Pobranie danych rekordu
    customer_record = Record.objects.get(id=record_id)

    # Tworzenie pliku Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Customer Record"

    # Dodanie nagłówków
    headers = [
        'ID', 'Date & Client name', 'vCPU', 'vRAM', 'Adm Hours', 'vConnect', 'Disk', 'Disk profile', 'PBS Backup',
        'PBS Replication', 'IP', 'Public Network Speed', 'Network', 'DMZ', 'Firewall Premium', 'GeoFirewall',
        'IPSec', 'SSL-VPN Accounts', 'DNS Guard', 'Webfiltering', 'IDS/IPS/AV', 'VDOM', 'Windows Server 2022 (1Y)',
        'Windows Server 2022 (3Y)', 'Windows Server 2022 CAL (1Y)', 'Windows Server 2022 CAL (3Y)', 'RDS CAL (1Y)',
        'RDS CAL (3Y)', 'RDS CAL (PERPETUAL)', 'Accepted', 'Status'
    ]
    
    # Wpisanie nagłówków
    for col_num, header in enumerate(headers, 1):
        ws.cell(row=1, column=col_num, value=header)

    # Wpisanie danych klienta
    data = [
        customer_record.id, f"{customer_record.created_at} {customer_record.client_name}",
        customer_record.vcpu, customer_record.vram, customer_record.adm_hours, customer_record.vconnect,
        customer_record.disk, customer_record.disk_profile, customer_record.pbs, customer_record.pbs_replication,
        customer_record.ip, customer_record.pub_net_speed, customer_record.network, customer_record.dmz,
        customer_record.fw_premium, customer_record.geofw, customer_record.ipsec, customer_record.ssl_vpn,
        customer_record.dns_guard, customer_record.webfiltering, customer_record.ids_ips, customer_record.vdom,
        customer_record.ws2022_1, customer_record.ws2022_3, customer_record.ws2022_cal_1, customer_record.ws2022_cal_3,
        customer_record.rds_cal_1, customer_record.rds_cal_3, customer_record.rds_cal_perpetual, customer_record.is_accepted,
        customer_record.status
    ]

    # Wpisanie danych wiersza
    for col_num, value in enumerate(data, 1):
        ws.cell(row=2, column=col_num, value=value)

    # Ustawienia odpowiedzi dla pliku Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename=customer_record_{customer_record.id}.xlsx'

    wb.save(response)
    return response