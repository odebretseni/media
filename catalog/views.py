from django.shortcuts import render
from .models import Item, Photo
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import Context, loader


@login_required
def index(request):
    item_list = Item.objects.all()
    return render(request, 'index.html', context={'item_list': item_list})


class ItemListView(LoginRequiredMixin, generic.ListView):
    model = Item


class ItemDetailView(LoginRequiredMixin, generic.DetailView):
    model = Item


class PhotoDetailView(LoginRequiredMixin, generic.DetailView):
    model = Photo


def error404(request):
    template = loader.get_template('404.html')
    context = Context({"message": "All: %s" % request, })
    return HttpResponse(content=template.render(context), content_type='text/html; charset=utf-8', status=404)




