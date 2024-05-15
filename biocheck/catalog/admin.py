from django.contrib import admin
from .models import FoodAdditives


class FoodAdditivesAdmin(admin.ModelAdmin):
    list_display = (
        'e_title',
        'common_title',
        'category',
        'description',
        'is_dangerous',
        'is_not_informative'
    )
    list_editable = (
        'common_title',
        'category',
        'description',
        'is_dangerous',
        'is_not_informative'
    )
    search_fields = (
        'e_title',
        'common_title'
    )
    list_filter = ('category', 'is_not_informative')
    list_display_links = ('e_title',)


admin.site.register(FoodAdditives, FoodAdditivesAdmin)
