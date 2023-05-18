from django.contrib import admin

from .models import *


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class SpecialistAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class OfferAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class NewbuildingAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}



admin.site.register(News, NewsAdmin)

admin.site.register(Specialist, SpecialistAdmin)

admin.site.register(Company, CompanyAdmin)

admin.site.register(Offer, OfferAdmin)

admin.site.register(Review)

admin.site.register(Rent)

admin.site.register(Newbuilding, NewbuildingAdmin)
