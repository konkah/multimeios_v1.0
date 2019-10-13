from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReservaForm
from .models import Sala

# Create your views here.
# Templates que serão visualizados no site

def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReservaForm(request.POST)
        # check whether it's valid:
        #if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReservaForm()

    salas = Sala.objects.all()
    return render(request, 'djreservas/index.html', {'form': form, 'salas': salas})

