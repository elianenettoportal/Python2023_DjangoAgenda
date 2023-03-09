from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from .models import Contact

def index(request):
    contactList = Contact.objects.order_by('last_name').filter(active=True)
    paginator = Paginator(contactList, 20)
    page = request.GET.get('p')
    contactList = paginator.get_page(page)

    return render(request, 'contacts/index.html',{
        'contacts':contactList
    })

def contact_profile(request, id):
    try:
        contact = Contact.objects.get(id=id)
        
        if not contact.active:
            messages.add_message(request,messages.INFO, 'Inactive contact' )
            return redirect('index')
        
        return render(request, 'contacts/contact_profile.html',{
            'contact':contact
        })
    except Contact.DoesNotExist as err:
        messages.add_message(request,messages.INFO, 'Contact Not Found!' )
        return redirect('index')


def search(request):
    termo = request.GET.get('termo')
   
    if termo is None or not termo:
        messages.add_message(request,messages.ERROR, 'Please, add a term for the search' )
        return redirect('index')
   
    contactList = Contact.objects.order_by('last_name').filter(
        Q(name__icontains= termo) | Q(last_name__icontains = termo),
        active=True
    )
    # print(contacts.query)
    paginator = Paginator(contactList, 20)
    page = request.GET.get('p')
    contactList = paginator.get_page(page)
    messages.add_message(request,messages.SUCCESS, 'Success' )
    return render(request, 'contacts/search.html',{
        'contacts':contactList
    })

def search2(request):
    termo = request.GET.get('termo')
    full_name = Concat('name',Value(' '), 'last_name')
    contactList = Contact.objects.annotate(
        name_lastName = full_name
    ).filter(
        name_lastName__icontains = termo
    )
    # print(contacts.query)
    paginator = Paginator(contactList, 20)
    page = request.GET.get('p')
    contactList = paginator.get_page(page)

    return render(request, 'contacts/search.html',{
        'contacts':contactList
    })