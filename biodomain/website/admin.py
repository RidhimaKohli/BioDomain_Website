from django.contrib import admin
from website.models import *
from import_export.admin import ImportExportModelAdmin
from .models import *
admin.site.register(Category_Description,ImportExportModelAdmin)
admin.site.register(Institute,ImportExportModelAdmin)
admin.site.register(Instruments,ImportExportModelAdmin)
#admin.site.register(Instrument_Description,ImportExportModelAdmin)

class ViewAdmin(ImportExportModelAdmin):
    pass
