from django.shortcuts import render


# Create your views here.
def login(request):
    server_data = {

    }
    return render(request, 'login.html', server_data)
