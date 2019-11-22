from django.shortcuts import render

# Create your views here.
def homeview(request):
    return render(request,'myapp/home.html')
def coursesview(request):
    return render(request,'myapp/courses.html')

def sportsview(request):
    return render(request,'myapp/sports.html')
def newsview(request):
    return render(request,'myapp/news.html')