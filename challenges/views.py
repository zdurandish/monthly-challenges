from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes a day!",
    "march": "Learn Django for at least 20 minutes a day!",
    "april": "Call your mom twice a week!",
    "may": "Work out for 1 hour every day!",
    "june": "Meditate for at least 10 minutes a day!",
    "july": "Read 10 pages of your favorite book every day!",
    "august": "Wake up at 5am twice a week!",
    "september": "Stick to a good skin care routine!",
    "october": "Plan a reunion with your friends!",
    "november": "Cut off a toxic relationship!",
    "december": "Drink 8 glasses of water every day!"
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("str-path", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month!")

    redirect_month = months[month - 1]
    redirect_path = reverse("str-path", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Invalid Input!</h1>")