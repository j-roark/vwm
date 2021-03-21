from django.shortcuts import render
from django.template import loader
from items.models import Category, Item

def Index(request):
    template_name = 'vietnamwarmilitaria/index.html'
    recents = [x for x in Item.objects.all()]
    recents.sort(reverse=True, key=Item.get_recents)
    context = {
        'recent_additions':recents[:2],
        'categories':[x for x in Category.objects.all()]
    }
    return render(request, template_name, context)
