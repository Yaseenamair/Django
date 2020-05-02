from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = ' The city that never sleeps'
    dest1.img = 'destination_1.jng'
    dest1.price = 599
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Chennai'
    dest2.desc = 'The IT city'
    dest2.img = 'destination_2.jng'
    dest2.price = 699
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Delhi'
    dest3.desc = 'The India Gate city'
    dest3.img = 'destination_3.png'
    dest3.price = 799
    dest3.offer = False


    dest4 = Destination()
    dest4.name = 'Hyderabad'
    dest4.desc = ' The Biryani city'
    dest4.img = 'destination_4.png'
    dest4.price = 899
    dest4.offer = True

    dests = [dest1, dest2, dest3, dest4]

    return render(request, "index.html", {'dests' : dests})