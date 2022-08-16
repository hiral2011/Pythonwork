
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

month_name = {
    "january":"eat no meat for entire month",
    "february":"walk for at least 20 minutes every day!",
    "march":"learn django at least 20 minutes every day!",
    "april":"no insta for whole month",
    "may":"focus to carrer", 
    "june":"no break month",
    "july":"no more code",
    "august":"holidays are here ",
    "september":"no cash back",
    "octomber":"eat health food for this month",
    "november":"this is birthday month",
    "december":"happy 31st month"
}

# Create your views here.

def index(request):
    list_items = ""
    months= list(month_name.keys())
    
    for month in months:
        capitalized_month=month.capitalize()
        month_path = reverse("month_challenge" , args=[month])
        list_items += f"<li><a href =\"{month_path }\">{capitalized_month}</a></li>"

    #"<li><a href="...">january</a></li><li><a href="...">february</a></li>..."
 
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def mypage_by_number(request,month):
    months= list(month_name.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month") 

    redirect_month=months[month - 1]
    redirect_path=reverse("month_challenge" , args=[redirect_month]) #challenge/january
    return HttpResponseRedirect(redirect_path)

def mypage(request, month):
    try:
        challenges_text = month_name[month]
        return render(request,"challenges/challenge.html",{
            "text":challenges_text,
            "month_name":month.capitalize()
        })
    except:
        return HttpResponseNotFound("this month is not found")
