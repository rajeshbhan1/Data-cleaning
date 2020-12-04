from django.contrib import admin
from .models import Airport
from import_export.admin import ImportExportModelAdmin


admin.site.register(Airport)
