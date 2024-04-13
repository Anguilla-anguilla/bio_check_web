from django.shortcuts import render
from models import FoodAdditives

def fa_list(request):
    template_name = 'catalog/fa_list.html'
    fa_catalog = FoodAdditives.objects.values(
        'e_title', 'common_title'
        ).order_by('e_title')
    context = {
        'fa_catalog': fa_catalog
    }
    return render(request, template_name, context)


def fa_detail(request):
    pass