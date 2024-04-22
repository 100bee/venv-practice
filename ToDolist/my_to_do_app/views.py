from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "my_to_do_app/index_init.html")