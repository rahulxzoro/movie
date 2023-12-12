from django.shortcuts import render,redirect
from . models import Movie
# Create your views here.
def home(request):
    obj=Movie.objects.all()
    return render(request,'index.html',{"result":obj})

def details(request,movie_id):
    data=Movie.objects.get(id=movie_id)
    return render(request,'details.html',{"data":data})

def movieRegister(request):
    if request.method=='POST':
       
        banner=request.FILES['banner']
        poster=request.FILES['poster']
        name=request.POST.get('name')
        rating=request.POST.get('rating')
        screen=request.POST.get('screen')
        language=request.POST.get('language')
        duration=request.POST.get('duration')
        category=request.POST.get('category')
        date=request.POST.get('date')
        
        movie=Movie(banner=banner,poster=poster,name=name,rating=rating,screen=screen,language=language,duration=duration,category=category,date=date)
        movie.save()
        return redirect('/')
    return render(request,'registerMovie.html')

def delete(request,details_id):
    if request.method=='POST':
        data=Movie.objects.get(id=details_id)
        data.delete()
        return redirect('/')
    return render(request,'delete.html')
    

