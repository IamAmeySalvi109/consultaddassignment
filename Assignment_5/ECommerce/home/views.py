from django.shortcuts import render
from signup.models import Product

# Create your views here.


def home(request):
    context = {
        'Products': Product.objects.all()
    }
    return render(request, 'home/home.html', context)


