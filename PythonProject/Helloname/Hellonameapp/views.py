from django.shortcuts import render
def home(request):
    name = request.GET.get('name', '')
    return render(request, 'Hellonameapp/home.html', {'name': name})

# Create your views here.
