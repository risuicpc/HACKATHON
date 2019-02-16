from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .models import *
from .forms import *


def index(request):
    return render(request, 'include/home.html', {})

def login(request):
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form' : form})

@login_required
def login_redirect(request):    
    if request.user.is_staff:
        return redirect('admin:index')
    else:
        object = []
        title  = None
        role =None
        for role in request.user.role.all():
            if role.role_name == 'rg_admin':
                object = Region.objects.filter(region_admin=request.user)
                title = 'zone'
                role = 'rg_admin'
                break
            elif role.role_name == 'zn_admin':
                object = Zone.objects.filter(zone_admin=request.user)
                title = 'werede'
                role = 'zn_admin'
                break
            elif role.role_name == 'wr_admin':
                object = Wereda.objects.filter(wereda_admin=request.user)
                title = 'kebele'
                role = 'wr_admin'
                break
            elif role.role_name == 'kb_admin':
                object = Kebele.objects.filter(kebele_admin=request.user)
                title = 'user'
                role = 'kb_admin'
                break
            elif role.role_name == 'org_admin':
                object = Rorgenization.objects.filter(rorgenization_admin=request.user)
                title = 'orgenization'
                role = 'org_admin'
                break
        
        context = {
            'object': object,
            'title': title,
            'role': role
        }
        return render(request, 'authentication/home.html', context)

def zone_add(request):
    form = ZoneCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            region = Region.objects.get(region_admin=request.user)
            user.region = region
            user.save()
            id = get_object_or_404(Zone, zone_name=request.POST['zone_name']).id
            messages.success(request, 'Zone "<a href="/zone/add/' + str(id) + '/edit/">' + request.POST["zone_name"] + '</a>" was added successfully.')
            if request.POST['save'] == 'save':
                return redirect('authentication:zonelist')
            else:
                form = ZoneCreateForm()
        else:
            messages.error(request, 'Zone was not added successfully. Please correct the error below.')

    context = {'form': form}
    return render(request, 'authentication/zone_add.html', context)

def zone_list(request):
    object = Region.objects.get(region_admin=request.user)
    zone   = Zone.objects.filter(region=object)
    
    context = {
        'zone': zone
    }
    return render(request, 'authentication/zone_list.html', context)

def user_add(request):
    exel = UserCreationExel()
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form.save_m2m()
            id = get_object_or_404(User, user_name=request.POST['user_name']).id
            messages.success(request, 'User "<a href="/user/add/' + str(id) + '/edit/">' + request.POST["user_name"] + '</a>" was added successfully.')
            if request.POST['save'] == 'save':
                return redirect('authentication:zonelist')
            else:
                form = UserCreationForm()
    context = {'form': form, 'exel' : exel,}
    return render(request, 'authentication/user_add.html', context)




def wereda_add(request):
    form = WeredaCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            region = Region.objects.get(region_admin=request.user)
            user.region = region
            user.save()
            id = get_object_or_404(Zone, zone_name=request.POST['zone_name']).id
            messages.success(request, 'Zone "<a href="/zone/add/' + str(id) + '/edit/">' + request.POST["zone_name"] + '</a>" was added successfully.')
            if request.POST['save'] == 'save':
                return redirect('authentication:zonelist')
            else:
                form = ZoneCreateForm()
        else:
            messages.error(request, 'Zone was not added successfully. Please correct the error below.')

    context = {'form': form}
    return render(request, 'authentication/zone_add.html', context)




def kebele_add(request):
    form = KebeleCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            wereda = Wereda.objects.get(region_admin=request.user)
            user.region = wereda
            user.save()
            id = get_object_or_404(Zone, zone_name=request.POST['zone_name']).id
            messages.success(request, 'Kebele "<a href="/kebele/add/' + str(id) + '/edit/">' + request.POST["kebele_name"] + '</a>" was added successfully.')
            if request.POST['save'] == 'save':
                return redirect('authentication:zonelist')
            else:
                form = KebeleCreationForm()
    context = {'form': form}
    return render(request, 'authentication/kebele_add.html', context)

@login_required
def user_exel(request):
    exel = UserCreationExel(request.POST, request.FILES)
    form = UserCreationForm()
    if request.method == 'POST':
        if form.is_valid():
            exel = UserCreationExel()
    messages.success(request, 'User was uploaded successfully.')
    context = {'form': form, 'exel' : exel,}
    return render(request, 'authentication/user_add.html', context)