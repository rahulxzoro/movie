
from django.urls import path
from . import views

app_name='bookapp'
urlpatterns = [
    path('', views.home, name='index'),

    path('details/<int:movie_id>/',views.details,name='details'),
    
    path('registerMovie/',views.movieRegister,name='registerMovie'),
    
    path('delete/<int:details_id>',views.delete,name='delete')
]
