import openpyxl
import re
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
            vcpu = request.POST.get("vcpu")
            vram = request.POST.get("vram")
            disk = request.POST.get("disk")
            pbs = request.POST.get("pbs")

            # Sprawdzanie czy wartości są liczbami przed konwersją do int
            if vcpu and not vcpu.isdigit():
                messages.error(request, "vCPU musi być liczbą!")
                return render(request, 'add_record.html', {'form': form})

            if vram and not vram.isdigit():
                messages.error(request, "vRAM musi być liczbą!")
                return render(request, 'add_record.html', {'form': form})

            if disk and not disk.isdigit():
                messages.error(request, "Dysk musi być liczbą!")
                return render(request, 'add_record.html', {'form': form})

            if pbs and not pbs.isdigit():
                messages.error(request, "PBS musi być liczbą!")
                return render(request, 'add_record.html', {'form': form})

            vcpu = int(vcpu) if vcpu else 0
            vram = int(vram) if vram else 0
            disk = int(disk) if disk else 0
            pbs = int(pbs) if pbs else 0

            # Sprawdzenie, czy vCPU i vRAM są zgodne z wymaganiami
            if vcpu > 32:
                messages.error(request, "Maksymalna dozwolona wartość vCPU to 32!")
                return render(request, 'add_record.html', {'form': form})

            if vram > 32:
                messages.error(request, "Maksymalna dozwolona wartość vRAM to 32!")
                return render(request, 'add_record.html', {'form': form})

            if disk < 20 or disk > 1000:
                messages.error(request, "Rozmiar dysku możliwy do wyboru to zakres od 20 do 1000!")
                return render(request, 'add_record.html', {'form': form})

            # Sprawdzenie, czy PBS jest taki sam jak Disk
            if pbs != disk:
                messages.error(request, "PBS musi być równy wartości dysku!")
                return render(request, 'add_record.html', {'form': form})

            if form.is_valid():
                form.save()
                messages.success(request, "Record Added...")
                return redirect('home')

        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "You must be logged in...")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        previous_is_accepted = current_record.is_accepted  # Pobranie starej wartości
        
        form = AddRecordForm(request.POST or None, instance=current_record)
        
        if form.is_valid():
            updated_record = form.save(commit=False)  # Zatrzymujemy zapis, aby sprawdzić zmiany
            
            # Jeśli użytkownik nie zmienił wartości is_accepted, to ustawiamy na 0
            if previous_is_accepted == updated_record.is_accepted:
                updated_record.is_accepted = 0

            updated_record.save()  # Zapisujemy zmiany
            
            messages.success(request, "Record has been updated...")
            return redirect('home')
        
        return render(request, 'update_record.html', {'form': form})
    
    else:
        messages.error(request, "You must be logged in to do that...")
        return redirect('home')

#Testy generowania wyceny

def generate_xlsx(request, record_id):
    # Pobranie rekordu z bazy danych
    customer_record = Record.objects.get(id=record_id)

    # Ścieżka do szablonu
    template_path = "website/templates/template_vps.xlsx"

    # Otwieramy plik Excel jako szablon
    wb = openpyxl.load_workbook(template_path)
    ws = wb.active

    # Dodajemy nazwę klienta do A1
    ws["A1"] = customer_record.client_name

    # Mapa wartości do podmiany
    data_map = {
        "vCPU": customer_record.vcpu,
        "RAM": customer_record.vram,
        "Dysk": customer_record.disk,
        "Backup": customer_record.pbs,
        "Strefa bezpieczeństwa": customer_record.dmz,
        "Sieć wewnętrzna - 1Gbit/s": customer_record.network,
        "Replikacja Backupu": customer_record.pbs_replication,
        "vConnect": customer_record.vconnect,
        "Adresacja IPv4": customer_record.ip,
        "Godziny administracyjne (h) - Tier III": customer_record.adm_hours,
        "Windows Server 2022 Standard - 8 Core License Pack 1 Year": customer_record.ws2022_1,
        "Windows Server 2022 Standard - 8 Core License Pack 3 Year": customer_record.ws2022_3,
        "Windows Server 2022 CAL - 1 User CAL - 1 year": customer_record.ws2022_cal_1,
        "Windows Server 2022 CAL - 1 User CAL - 3 year": customer_record.ws2022_cal_3,
        "Windows Server 2022 Remote Desktop Services - 1 User CAL 1 Year": customer_record.rds_cal_1,
        "Windows Server 2022 Remote Desktop Services - 1 User CAL 3 Year": customer_record.rds_cal_3,
        "Windows Server 2022 Remote Desktop Services - 1 Device CAL - perpetual": customer_record.rds_cal_perpetual,
        "Data Space Shield - Firewall Premium - 10 reguł": customer_record.fw_premium,
        "Data Space Shield - Geo Firewall - 1 kraj": customer_record.geofw,
        "Data Space Shield - IPSEC": customer_record.ipsec,
        "Data Space Shield - SSL VPNs": customer_record.ssl_vpn,
        "Data Space Shield - Guard DNS": customer_record.dns_guard,
        "Data Space Shield - Webfiltering": customer_record.webfiltering,
        "Data Space Shield - IDS/IPS/AV - 100 Mbit/s": customer_record.ids_ips,
        "Data Space Shield - vDOM": customer_record.vdom,
    }

    # Obsługa profilu wydajnościowego dysku
    disk_profile_row = {1: 10, 2: 11, 3: 12}  # Mapowanie profilu na wiersz w Excelu
    if customer_record.disk_profile in disk_profile_row:
        row_idx = disk_profile_row[customer_record.disk_profile]
        ws[f"C{row_idx}"] = 1  # Wstawienie wartości 1 do odpowiedniego wiersza

    # Obsługa zmiennej dmz
    if customer_record.dmz == '0':
        ws["C14"].value = 1
        ws["C15"].value = None  # Usunięcie wartości z C15, jeśli wcześniej coś tam było
    elif customer_record.dmz == '1':
        ws["C15"].value = 1
        ws["C14"].value = None  # Usunięcie wartości z C14, jeśli wcześniej coś tam było

    # Przygotowanie pliku do pobrania
    client_name = re.sub(r'[^a-zA-Z0-9_-]', '_', customer_record.client_name)  # Usunięcie znaków specjalnych
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename=wycena_vps_{client_name}.xlsx'

    wb.save(response)
    return response
