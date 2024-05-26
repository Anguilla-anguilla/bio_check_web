from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import FoodAdditives


def fa_list(request):
    template_name = 'catalog/fa_list.html'
    fa_catalog = FoodAdditives.objects.values('id',
                                              'e_title',
                                              'common_title',
                                              'category'
                                              ).order_by('e_title')
    query = request.GET.get('search')
    if query:
        fa_catalog = fa_catalog.filter(
            Q(e_title__icontains=query) |
            Q(common_title__icontains=query)
        )
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
