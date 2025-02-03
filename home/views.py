from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """" A Veiw to retuen the index page """
    return render(request, 'home/index.html')