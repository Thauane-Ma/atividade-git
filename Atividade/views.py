from django.shortcuts import render

# Create your views here.
def thauane(request):
    return render(request, 'thauane.html')

def luis(request):
    return render(request, 'luis.html')
