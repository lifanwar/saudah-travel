from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Package

def package_list(request):
    packages = Package.objects.all()
    context = {'packages': packages}
    return render(request, 'packages/package_list.html', context)

def package_detail(request, pk):
    package = get_object_or_404(Package, pk=pk)
    context = {'package': package}
    return render(request, 'packages/package_detail.html', context)
