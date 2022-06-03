from django.http import HttpResponse
from django.shortcuts import redirect, render
from bunny.forms import MyPetForm

def home(request):
    return render(request, 'bunny/index.html')


def myPetCreateView(request):
    if request.method == 'POST':
        form = MyPetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')

    else:
        form = MyPetForm()

    return render(request, 'bunny/my-pet.html', {'form': form})
