from django.shortcuts import render
from .models import Genre, Show
# Create your views here.

def index(request):
    shows = Show.objects.all()

    context = {'shows' : shows}
    return render(request, 'sitcoms/index.html',context)