from django.urls import path
from . import views 

urlpatterns = [
    path("" ,views.index), #/challenges/
    path("<int:month>",views.mypage_by_number),
    path("<str:month>",views.mypage,name="month_challenge")    
]