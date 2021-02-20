from django.shortcuts import render
from listing.models import Listing
from realtors.models import Realtors
from listing.choices.choice import bedroom_choices,state_choices,price_choices
from django.http import HttpResponse

def index(request):
    k=Listing.objects.all().order_by('-list_date')[:3]
    context={"li":k,"bedroom_choices":bedroom_choices,"state_choices":state_choices,"price_choices":price_choices}
    return render(request,'pages/index.html',context)
def about(request):
    r=Realtors.objects.all()
    sm=Realtors.objects.filter(is_mvp=True)

    context={"real":r,"sm":sm}

    return render(request,'pages/about.html',context)


# Create your views here.
