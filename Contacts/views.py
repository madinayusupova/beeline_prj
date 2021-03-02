from django.shortcuts import render
from .models import Contact
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


# Create your views here.
def contacts_list(request):
    name_list = Contact.objects.all()
    contacts_per_page = 4
    paginator = Paginator(name_list, contacts_per_page)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
        page_num = int(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
        page_num = 1
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
        page_num = paginator.num_pages

    start_num = 1+(page_num-1)*contacts_per_page
    return render(request, 'Contacts/home.html', {'contacts': contacts, 'page': page, 'start_num':start_num})


def search(request):
    query = request.GET.get('q')
    contacts = Contact.objects.filter(Q(name__icontains=query) | Q(phone_number__icontains=query))
    if contacts:
        return render(request, 'Contacts/search.html', {'contacts': contacts, "query": query})

    else:
        text = "Sorry, nothing found"
        return render(request, 'Contacts/search.html', {'contacts': contacts, 'text': text, "query": query})
