from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Item


def index_view(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "home/index.html", context=context)


def create_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        item = Item(name=name)
        item.save()
        return HttpResponse(f'<li class="text-8xl fint-thin">{item.name}</li>')
    else:
        redirect("home:home-index")
