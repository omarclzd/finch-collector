from django.shortcuts import render
from django.http import HttpResponse

class Finch:
  def __init__(self, name, description, age):
    self.name = name
    self.description = description
    self.age = age

finchs = [
  Finch('finchone', 'bird1', 3),
  Finch('finchtwo', 'bird2', 2),
  Finch('finchthree', 'bird3', 1)
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello Bird</h1>')


def about(request):
  return render(request, 'about.html') 

def finchs_index(request):
  return render(request, 'finchs/index.html', {'finchs': finchs})