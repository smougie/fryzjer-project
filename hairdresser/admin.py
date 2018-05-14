from django.contrib import admin

# Register your models here.
from hairdresser.models import News, Barbers, CompletedCourses, SalonInfo, PriceTable, Products

admin.site.register(News)
admin.site.register(Barbers)
admin.site.register(CompletedCourses)
admin.site.register(SalonInfo)
admin.site.register(PriceTable)
admin.site.register(Products)

