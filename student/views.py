from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'student/index.html')


def showall(request):
    return render(request, 'student/showall.html')


def update(request):
    return render(request, 'student/update.html')


def delete(request):
    return render(request, 'student/delete.html')
