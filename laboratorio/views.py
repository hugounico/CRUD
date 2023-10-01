from django.shortcuts import render

# Create your views here.
def read_labs(request):                                  
    return render(request, 'laboratorio/read_labs.html')