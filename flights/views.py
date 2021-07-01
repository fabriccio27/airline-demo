from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger
# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except:
        return HttpResponse("Couldn't get info for that flight, why? Probably doesn't exist")

    return render(request, "flights/flight.html", {
        "flight":flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
        # con esto arma las options del select, excluir de Passenger a los que tienen este vuelo en sus vuelos.

    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        passenger.flights.add(flight)
        # la coma en args es para que me tome como un tuple,y no como argumentos
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
