from django.contrib import admin
from website.models import Equipments
from import_export.admin import ImportExportModelAdmin
from .models import *
admin.site.register(Equipments,ImportExportModelAdmin)

class ViewAdmin(ImportExportModelAdmin):
    pass
