from django.shortcuts import render

# Create your views here.
# Templates que serão visualizados no site

def index(request):
    return render(request, 'djreservas/index.html')
def forms(resquest):
    return render(request, 'djreservas/forms.html')