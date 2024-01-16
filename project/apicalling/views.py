from django.shortcuts import render

# Create your views here.

def Welcome(request):
    return render(request , 'form.html')
def User(request):
    username = request.GET['username']
    return render(request, 'user.html', {'name':username})