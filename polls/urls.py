from django.urls import path

from . import views

app_name='polls'
urlpatterns = [
    path('',views.index,name="index"),
    path('<int:questions_id>/',views.details,name="details"),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/result/', views.result, name='result'),
    
]   
