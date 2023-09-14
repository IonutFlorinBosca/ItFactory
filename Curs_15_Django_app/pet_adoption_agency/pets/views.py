from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pet


# Aici se decide ce apare in pagina (restul sunt legaturi intre care aduc spre 'view')

# Create your views here.
def index(request):
    return HttpResponse('Hello from pets_index')


def pets(request):
    pets_list = Pet.objects.all()
    return render(request, 'all_pets.html', {'pets': pets_list})


def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    return render(request, 'pet_detail.html', {'pet': pet})
