from django.shortcuts import render

# Create your views here.
def beranda(request):
    return render(request, "core/beranda.html")

def about(request):
    return render(request, 'core/about.html')