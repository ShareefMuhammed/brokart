from django.shortcuts import render

# Create your views here.
def show_carts(request):
    return render(request, 'cart.html')