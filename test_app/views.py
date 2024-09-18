from django.shortcuts import render
from .models import Data


# Create your views here.
def index(request):
    data_users = Data.objects.all().values()  # TODO Implement this
    response = {"data_users": data_users}
    return render(request, "index.html", response)
