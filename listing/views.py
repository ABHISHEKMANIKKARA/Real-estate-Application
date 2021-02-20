from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator
from listing.choices.choice import bedroom_choices,state_choices,price_choices


# Create your views here.
def listings(request):
    li=Listing.objects.all()
    paginator=Paginator(li,1)
    page=request.GET.get('page')
    page_obj=paginator.get_page(page)
    list={"li":page_obj}
    return render(request,'listing/listings.html',list)
def listing(request,listing_id):
   ob= Listing.objects.filter(id=listing_id)
   context={"obj":ob}
   return render(request,'listing/listing.html',context)

def search(request):
    qset=Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        if(request.GET['keywords']):
            qset=qset.filter(description__icontains=request.GET['keywords'])
    if 'city' in request.GET:
        if (request.GET['city']):
                qset = qset.filter(city__iexact=request.GET['city'])
    if 'state' in request.GET:
        if (request.GET['state']):
                qset = qset.filter(state__icontains=request.GET['state'])

    context = {"bedroom_choices": bedroom_choices, "state_choices": state_choices,
               "price_choices": price_choices,"li":qset,"values":request.GET}
    return render(request,'listing/search.html',context)