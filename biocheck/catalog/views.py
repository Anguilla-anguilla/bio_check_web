from django.shortcuts import render, get_object_or_404
from .models import FoodAdditives

def fa_list(request):
    template_name = 'catalog/fa_list.html'
    fa_catalog = FoodAdditives.objects.values(
        'e_title', 'common_title'
        ).order_by('e_title')
    context = {
        'fa_catalog': fa_catalog
    }
    return render(request, template_name, context)


def fa_detail(request, pk):
    template_name = 'catalog/fa_detail.html'
    fa_card = get_object_or_404(
        FoodAdditives.objects.values('e_title',
                                      'common_title',
                                      'category',
                                      'description'),
        pk=pk
        )
    context = {
        'fa_card': fa_card,
    }
    return render(request, template_name, context)