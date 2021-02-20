from django.shortcuts import redirect
from .models import Contacts

# Create your views here.
def contacts(request):
    if request.method=="POST":
        user_id=request.POST['user_id']
        name=request.POST['name']
        list_id=request.POST['list_id']
        listing_name=request.POST['listing_name']
        email=request.POST['email']
        realtor_email = request.POST['realtor_email']
        phone = request.POST['phone']
        message = request.POST['message']
        us=Contacts(message=message,phone=phone,email=email,listing_id=list_id,name=name,user_id=user_id,listing_name=listing_name)
        us.save()
        return redirect('listing',listing_id=list_id)