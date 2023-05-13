from django.contrib import admin

from .models import *


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class SpecialistAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(News, NewsAdmin)

admin.site.register(Specialist, SpecialistAdmin)

admin.site.register(Company, CompanyAdmin)