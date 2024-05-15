from django.contrib import admin
from .models import FoodAdditives


class FoodAdditivesAdmin(admin.ModelAdmin):
    list_display = (
        'e_title',
        'common_title',
        'category',
        'description',
        'is_dangerous',
        'is_informative'
    )
    list_editable = (
        'is_dangerous',
        'is_informative'
    )
    search_fields = (
        'e_title',
        'common_title'
    )
    list_filter = ('category', 'is_informative')
    list_display_links = ('e_title',)
    empty_value_display = 'Информация дополняется.'


admin.site.register(FoodAdditives, FoodAdditivesAdmin)
