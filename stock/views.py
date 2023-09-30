# stock > views.py

from django.shortcuts import render
from .forms import ProductForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        #Almacenando los datos enviados por el usuario
        form = ProductForm(request.POST)
        #Si el formulario es valido, se guarda en el modelo
        if form.is_valid():
            form.save()
            return render(request, 'stock/index.html', {'form':form})
    else:
        form = ProductForm()
        return render(request, 'stock/index.html', {'form':form})