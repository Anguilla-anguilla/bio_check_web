from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from import_export.widgets import ForeignKeyWidget
from import_export import resources
from import_export import fields
from .models import FoodAdditives


class FAResourse(resources.ModelResource):
    class Meta:
        model = FoodAdditives


class FoodAdditivesAdmin(ImportExportActionModelAdmin):
    resource_class = FAResourse
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

