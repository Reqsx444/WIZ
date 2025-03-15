import openpyxl
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddRecordForm
from .models import Record
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from openpyxl import load_workbook

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
    # Pobranie rekordu z bazy danych
    customer_record = Record.objects.get(id=record_id)

    # Ścieżka do szablonu (dostosuj ścieżkę, jeśli plik jest w innym miejscu)
    template_path = "website/templates/template_vps.xlsx"

    # Otwieramy plik Excel jako szablon
    wb = openpyxl.load_workbook(template_path)
    ws = wb.active

    # **Dodajemy nazwę klienta do A1**
    ws["A1"] = customer_record.client_name

    # Mapa wartości do podmiany (klucz -> wartość)
    data_map = {
        "vCPU": customer_record.vcpu,
        "RAM": customer_record.vram,
        "Dysk": customer_record.disk,
        "Profil wydajnościowy dysku": customer_record.disk_profile,
        "Backup": customer_record.pbs,
        "Replikacja Backup": customer_record.pbs_replication,
        "Adresacja IPv4": customer_record.ip,
        "Sieć wewnętrzna - 1Gbit/s": customer_record.network,
        "Firewall Premium": customer_record.fw_premium,
        "Data Space Shield - IPSec": customer_record.ipsec,
        "Data Space Shield - SSL-VPN": customer_record.ssl_vpn,
        "Data Space Shield - Webfiltering": customer_record.webfiltering,
        "Data Space Shield - IDS/IPS/AV - 100 Mbit/s": customer_record.ids_ips,
        "Windows Server 2022 (1Y)": customer_record.ws2022_1,
        "Windows Server 2022 (3Y)": customer_record.ws2022_3,
    }

    # Podmiana wartości w kolumnie C na podstawie nazw w kolumnie A
    for row in ws.iter_rows(min_row=1, max_row=ws.max_row):
        cell_a = row[0]  # Komórka w kolumnie A

        if cell_a.value in data_map:  # Jeśli nazwa pasuje do klucza w słowniku
            cell_c = row[2]  # Komórka w kolumnie C (indeks 2)
            cell_c.value = data_map[cell_a.value]  # Wstawienie wartości

    # Przygotowanie pliku do pobrania
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename=customer_record_{customer_record.id}.xlsx'

    wb.save(response)
    return response