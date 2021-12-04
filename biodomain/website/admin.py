from django.contrib import admin
from website.models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import *
admin.site.register(Categories,ImportExportModelAdmin)
admin.site.register(Institute,ImportExportModelAdmin)
admin.site.register(Instruments,ImportExportModelAdmin)
#admin.site.register(Instrument_Description,ImportExportModelAdmin)

class ViewAdmin(ImportExportModelAdmin):
    pass

class instrumentResource(resources.ModelResource):
    class Meta:
        model = Instruments
        exclude = ('id',)
        import_id_fields = ('iid',)
        fields = ('iid', 'instrumentname','category','instrumentquantity','instrumentdescription','institute')