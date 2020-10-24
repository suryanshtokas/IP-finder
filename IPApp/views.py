from django.shortcuts import render
import ipapi

def index(request):
    search = request.POST.get('search')
    data = ipapi.location(ip=search, output="json")

    context = {"data": data}

    return render(request, 'index.html', context)

def finder(request):
    search = get_client_ip(request)
    data = ipapi.location(ip=search, output="json")

    context = {"data": data}

    return render(request, 'finder.html', context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip